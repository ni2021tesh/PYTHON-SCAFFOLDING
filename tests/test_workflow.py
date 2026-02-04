"""Basic workflow tests."""
from app.agents.workflow import build_workflow


def test_workflow_runs():
    workflow = build_workflow()
    result = workflow({"input": "value"})
    assert result["payload"]["enriched"] is True
    assert result["steps"] == ["start", "finish"]
