from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
  mongodb_url: str
  mongodb_dbname: str

  class Config:
    env_file = ".env"

@lru_cache
def get_settings():
  return Settings()
