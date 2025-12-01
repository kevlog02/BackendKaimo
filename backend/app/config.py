from pydantic_settings import BaseSettings
from typing import Optional
import os


CURRENT_ENV = os.getenv("ENV", os.getenv("RAILWAY_ENVIRONMENT", "development")).lower()


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "")
    secret_key: str = os.getenv("SECRET_KEY", "INSECURE_DEV_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")

    EMAILS_FROM_EMAIL: str = os.getenv("EMAILS_FROM_EMAIL", "")
    EMAILS_FROM_NAME: str = os.getenv("EMAILS_FROM_NAME", "Kaimo")

    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")

    frontend_url: str = os.getenv("FRONTEND_URL", "")
    api_url: str = os.getenv("API_URL", "")

    environment: str = CURRENT_ENV
    debug: bool = CURRENT_ENV != "production"
    docs_enabled: bool = CURRENT_ENV != "production"

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"



settings = Settings()


def is_production() -> bool:
    return settings.environment == "production"


def get_cors_origins() -> list:
    if is_production():
        return [settings.frontend_url]

    return [
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ]
