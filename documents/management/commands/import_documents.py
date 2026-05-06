"""
Import learning documents from a JSON or CSV file.

JSON format:
  See data/examples/documents_sample.json for a complete example.

CSV format:
  Columns: title_he, description_he, file_url, file_type,
           domain_slug, tags (comma-separated tag slugs)

Flags:
  --dry-run   Preview without saving.
  --update    Update existing documents matched by file_url.
"""
import csv
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from content.models import Domain
from documents.models import LearningDocument, DocumentTag, FileType


class Command(BaseCommand):
    help = "Import learning documents from JSON or CSV"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help="Path to JSON or CSV file")
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--update", action="store_true")

    def handle(self, *args, **options):
        path = Path(options["path"])
        if not path.exists():
            raise CommandError(f"File not found: {path}")

        dry_run = options["dry_run"]
        allow_update = options["update"]

        if path.suffix.lower() == ".json":
            rows = self._load_json(path)
        elif path.suffix.lower() == ".csv":
            rows = self._load_csv(path)
        else:
            raise CommandError("File must be .json or .csv")

        self.stdout.write(f"Loaded {len(rows)} documents from {path.name}")
        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN — nothing will be saved"))

        created = updated = skipped = errors = 0

        for i, row in enumerate(rows, 1):
            try:
                result = self._process_row(row, dry_run=dry_run, allow_update=allow_update)
                if result == "created":
                    created += 1
                elif result == "updated":
                    updated += 1
                elif result == "skipped":
                    skipped += 1
            except Exception as exc:
                errors += 1
                self.stderr.write(f"  [ERROR] row {i} — {exc}")

        self.stdout.write(f"\n  Created: {created}  Updated: {updated}  Skipped: {skipped}  Errors: {errors}")
        if errors:
            self.stdout.write(self.style.WARNING(f"Completed with {errors} error(s)."))
        else:
            self.stdout.write(self.style.SUCCESS("Import complete."))

    def _load_json(self, path: Path) -> list[dict]:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise CommandError("JSON root must be an array.")
        return data

    def _load_csv(self, path: Path) -> list[dict]:
        rows = []
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append({
                    "title_he": row.get("title_he", "").strip(),
                    "description_he": row.get("description_he", "").strip(),
                    "file_url": row.get("file_url", "").strip(),
                    "file_type": row.get("file_type", "pdf").strip(),
                    "domain_slug": row.get("domain_slug", "").strip(),
                    "tags": [t.strip() for t in row.get("tags", "").split(",") if t.strip()],
                })
        return rows

    @transaction.atomic
    def _process_row(self, row: dict, dry_run: bool, allow_update: bool) -> str:
        title = row.get("title_he", "").strip()
        file_url = row.get("file_url", "").strip()

        if not title:
            raise ValueError("title_he is required")
        if not file_url:
            raise ValueError("file_url is required")

        domain_slug = row.get("domain_slug", "").strip()
        try:
            domain = Domain.objects.get(slug=domain_slug)
        except Domain.DoesNotExist:
            raise ValueError(f"Domain '{domain_slug}' not found")

        file_type = row.get("file_type", FileType.PDF).strip()
        if file_type not in FileType.values:
            raise ValueError(f"Invalid file_type '{file_type}'. Valid: {FileType.values}")

        existing = LearningDocument.objects.filter(file_url=file_url).first()
        if existing and not allow_update:
            self.stdout.write(f"  [skip] {title}")
            return "skipped"

        action = "updated" if existing else "created"
        self.stdout.write(f"  [{action}] {title}")

        if dry_run:
            return action

        if existing:
            existing.title_he = title
            existing.description_he = row.get("description_he", "")
            existing.file_type = file_type
            existing.domain = domain
            existing.save()
            doc = existing
        else:
            doc = LearningDocument.objects.create(
                title_he=title,
                description_he=row.get("description_he", ""),
                file_url=file_url,
                file_type=file_type,
                domain=domain,
            )

        doc.tags.clear()
        for slug in row.get("tags", []):
            tag = DocumentTag.objects.filter(slug=slug).first()
            if tag:
                doc.tags.add(tag)

        return action
