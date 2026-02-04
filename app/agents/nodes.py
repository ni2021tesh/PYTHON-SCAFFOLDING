"""Workflow nodes for the agent."""
from app.agents.state import AgentState


def start_node(state: AgentState) -> AgentState:
    """Initialize the workflow."""
    state.steps.append("start")
    return state


def finish_node(state: AgentState) -> AgentState:
    """Finalize the workflow."""
    state.steps.append("finish")
    return state
