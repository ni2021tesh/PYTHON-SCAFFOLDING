"""Base protocol definitions for repositories."""
from typing import Protocol


class Repository(Protocol):
    """Protocol for data repositories."""

    def get(self, key: str) -> dict:
        """Retrieve a record by key."""
        ...

    def save(self, key: str, payload: dict) -> None:
        """Persist a record by key."""
        ...
