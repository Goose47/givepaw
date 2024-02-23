from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class ConfigJWT(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_TTL: int = 30
    REFRESH_TOKEN_TTL: int = 60 * 24


settings_jwt = ConfigJWT()
