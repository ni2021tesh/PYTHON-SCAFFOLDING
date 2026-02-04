"""Service for orchestrating agent workflows."""
from app.agents.workflow import build_workflow
from app.utils.logger import configure_logger


class AgentService:
    """Primary service to run the agent workflow."""

    def __init__(self) -> None:
        self._logger = configure_logger(self.__class__.__name__)
        self._workflow = build_workflow()

    def run(self, payload: dict) -> dict:
        """Execute the workflow with the given payload."""
        self._logger.info("Running workflow")
        return self._workflow(payload)
