"""
One-time command: replace broken course slugs (generated from Hebrew) with
the canonical English slugs defined in seed_data.COURSES.
Safe to run multiple times — idempotent.
"""
from django.core.management.base import BaseCommand
from content.models import Course, Module

COURSE_SLUGS = {
    1:  "c01-re-finance-basics",
    2:  "c02-market-analysis",
    3:  "c03-property-valuation",
    4:  "c04-financial-metrics",
    5:  "c05-cash-flow-analysis",
    6:  "c06-deal-structure",
    7:  "c07-risk-management",
    8:  "c08-legal-documents",
    9:  "c09-advanced-models",
    10: "c10-risk-scenarios",
    11: "c11-credit-memo",
    12: "c12-capstone",
}

MODULE_SLUGS = {
    # (course_number, module_number): slug
    (1, 4): "ltv-dscr",
}


class Command(BaseCommand):
    help = "Fix course and module slugs to use English-only values"

    def handle(self, *args, **options):
        fixed = 0
        for course_number, correct_slug in COURSE_SLUGS.items():
            updated = Course.objects.filter(course_number=course_number).exclude(slug=correct_slug).update(slug=correct_slug)
            if updated:
                self.stdout.write(f"  Fixed C{course_number:02d} -> {correct_slug}")
                fixed += updated

        for (cn, mn), correct_slug in MODULE_SLUGS.items():
            updated = Module.objects.filter(course__course_number=cn, module_number=mn).exclude(slug=correct_slug).update(slug=correct_slug)
            if updated:
                self.stdout.write(f"  Fixed C{cn:02d}-M{mn:02d} -> {correct_slug}")
                fixed += updated

        if fixed:
            self.stdout.write(self.style.SUCCESS(f"Fixed {fixed} slug(s)."))
        else:
            self.stdout.write("All slugs already correct.")
