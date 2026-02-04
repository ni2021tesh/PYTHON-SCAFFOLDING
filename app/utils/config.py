"""Configuration helpers for the application."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    """Application configuration values loaded from environment."""

    app_name: str
    log_level: str



def load_config() -> AppConfig:
    """Load configuration from environment variables."""
    return AppConfig(
        app_name=os.getenv("APP_NAME", "my-agentic-project"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
