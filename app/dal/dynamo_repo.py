"""Example DynamoDB repository implementation."""
from app.dal.base import Repository


class DynamoRepository(Repository):
    """Placeholder DynamoDB repository."""

    def __init__(self) -> None:
        self._store: dict[str, dict] = {}

    def get(self, key: str) -> dict:
        return self._store.get(key, {})

    def save(self, key: str, payload: dict) -> None:
        self._store[key] = payload
