"""ECS entrypoint."""
from app.api.router import handle_request


if __name__ == "__main__":
    result = handle_request({"source": "ecs"})
    print(result)
