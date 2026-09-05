from pydantic_settings import BaseSettings
from os import getenv

class Settings(BaseSettings):
    # Секретный ключ должен совпадать с тем, что в Auth Service
    DATABASE_URL: str = getenv("DATABASE_URL", "DATABASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()
