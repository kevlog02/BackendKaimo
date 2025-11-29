from pydantic_settings import BaseSettings
from typing import Optional

CURRENT_ENV = 'development'

ENVIRONMENTS = {
    'development': {
        'database_url': 'mysql+pymysql://root:Kevin0224@localhost/kaimo_bd',
        'frontend_url': 'http://localhost:4200',
        'api_url': 'http://localhost:8000',
        'debug': True,
        'docs_enabled': True,
    },
    'production': {
        'database_url': 'mysql+pymysql://usuario:password@host.com/kaimo_bd',
        'frontend_url': 'https://kaimo.vercel.app',
        'api_url': 'https://kaimo-api.railway.app',
        'debug': False,
        'docs_enabled': False,
    }
}

# Obtener configuración actual
current_config = ENVIRONMENTS[CURRENT_ENV]

class Settings(BaseSettings):
    # Database
    database_url: str = current_config['database_url']
    
    # Security
    secret_key: str = "Kevronico0224"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Email
    email_host: str = "smtp.gmail.com"
    email_port: int = 587
    email_username: str = ""
    email_password: str = ""
    
    # Gemini AI
    gemini_api_key: Optional[str] = None
    
    # URLs
    frontend_url: str = current_config['frontend_url']
    api_url: str = current_config['api_url']
    
    # Environment
    environment: str = CURRENT_ENV
    debug: bool = current_config['debug']
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"

settings = Settings()

def is_production() -> bool:
    return CURRENT_ENV == "production"

def get_cors_origins() -> list:
    if is_production():
        return [settings.frontend_url]
    else:
        return [
            "http://localhost:4200",
            "http://127.0.0.1:4200",
        ]