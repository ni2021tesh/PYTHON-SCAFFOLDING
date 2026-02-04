"""AWS Lambda handler."""
from app.api.router import handle_request


def handler(event, context):
    """Lambda entrypoint."""
    payload = event.get("payload", {}) if isinstance(event, dict) else {}
    return handle_request(payload)
