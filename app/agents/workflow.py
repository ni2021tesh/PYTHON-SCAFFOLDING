"""Workflow assembly for the agent."""
from app.agents.nodes import finish_node, start_node
from app.agents.state import AgentState
from app.agents.tools import enrich_payload


def build_workflow():
    """Create a callable workflow."""

    def run(payload: dict) -> dict:
        state = AgentState(payload=enrich_payload(payload))
        state = start_node(state)
        state = finish_node(state)
        return {"payload": state.payload, "steps": state.steps}

    return run
