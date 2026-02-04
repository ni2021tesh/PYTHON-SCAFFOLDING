"""Shared state for the agent workflow."""
from dataclasses import dataclass, field


@dataclass
class AgentState:
    """Minimal state container for the agent workflow."""

    payload: dict
    steps: list[str] = field(default_factory=list)
