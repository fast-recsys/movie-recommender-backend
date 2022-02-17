from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
  mongodb_url: str
  mongodb_dbname: str
  mongodb_users_collection_name: str
  tmdb_base_url: str
  tmdb_images_base_url: str
  tmdb_api_key: str

  class Config:
    env_file = ".env"

@lru_cache
def get_settings():
  return Settings()
