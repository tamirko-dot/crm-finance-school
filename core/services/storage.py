from __future__ import annotations

import logging
from typing import BinaryIO

from django.conf import settings
from supabase import create_client, Client

logger = logging.getLogger(__name__)

_client: Client | None = None


def _get_client() -> Client:
    global _client
    if _client is None:
        _client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)
    return _client


class StorageService:
    """Abstraction over Supabase Storage. Swap implementation here only — no model or view changes needed."""

    def __init__(self, bucket: str | None = None):
        self.bucket = bucket or settings.SUPABASE_STORAGE_BUCKET

    def upload(self, file: BinaryIO, key: str, content_type: str = "application/octet-stream") -> str:
        client = _get_client()
        data = file.read()
        client.storage.from_(self.bucket).upload(
            path=key,
            file=data,
            file_options={"content-type": content_type, "upsert": "true"},
        )
        logger.info("Uploaded file to storage: %s", key)
        return key

    def get_url(self, key: str) -> str:
        client = _get_client()
        response = client.storage.from_(self.bucket).get_public_url(key)
        return response

    def delete(self, key: str) -> None:
        client = _get_client()
        client.storage.from_(self.bucket).remove([key])
        logger.info("Deleted file from storage: %s", key)

    def list(self, prefix: str = "") -> list[dict]:
        client = _get_client()
        return client.storage.from_(self.bucket).list(prefix)
