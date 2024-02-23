from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class AppConfig(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    UVICORN_APP_NAME: str
    UVICORN_HOST: str
    UVICORN_PORT: int
    UVICORN_RELOAD: bool

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_NAME: str
    POSTGRES_ECHO: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


settings_app = AppConfig()
