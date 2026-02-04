"""Registry of tools available to the agent."""


def list_tools() -> list[str]:
    """Return the names of registered tools."""
    return ["search", "summarize", "classify"]
