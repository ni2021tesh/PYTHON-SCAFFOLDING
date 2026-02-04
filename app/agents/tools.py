"""Tooling helpers for the agent."""


def enrich_payload(payload: dict) -> dict:
    """Sample tool to enrich a payload."""
    enriched = payload.copy()
    enriched["enriched"] = True
    return enriched
