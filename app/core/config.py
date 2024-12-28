"""
Config file
"""

import os

from dotenv import load_dotenv

load_dotenv(".env")


class Settings:
    """
    A class that encapsulates environment configuration variables.

    The Settings class retrieves sensitive configuration values such as API keys,
    database connection details, and other environment-specific settings from
    environment variables. Default values are provided if the environment variables
    are not set."""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DB_NAME}",
    )


settings = Settings()
