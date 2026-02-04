"""CLI entrypoint for local runs."""
import json
from app.api.router import handle_request


def main() -> None:
    """Run the agent workflow from the command line."""
    result = handle_request({"source": "cli"})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
