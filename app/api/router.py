"""API router placeholder."""
from app.services.agent_service import AgentService


def handle_request(payload: dict) -> dict:
    """Handle incoming API requests."""
    service = AgentService()
    return service.run(payload)
