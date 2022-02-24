# See: https://docs.pytest.org/en/latest/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

import asyncio
from typing import Any
import httpx
import pytest
from asgi_lifespan import LifespanManager
import pandas as pd

# Override configuration variables for tests
import os
from app.config import Settings
from app.data import get_movie_details_from_tmdb, get_movie_df, get_tmdb_id
from app.models.movie import MoviePublic

os.environ["MONGODB_URL"] = "mongodb://localhost:27017"
os.environ["MONGODB_DBNAME"] = "movie-rec"
os.environ["MONGODB_USERS_COLLECTION_NAME"] = "users"
os.environ["TMDB_BASE_URL"] = ""
os.environ["TMDB_IMAGES_BASE_URL"] = ""
os.environ["TMDB_API_KEY"] = ""

from app.main import app

@pytest.fixture(scope="session")
def event_loop():
  loop = asyncio.get_event_loop()
  yield loop
  loop.close()

def mock_get_movie_df() -> Any:
  mock_data = { 'movieId': [1], 'imdbId': [321], 'tmdbId': [123] }
  return pd.DataFrame(mock_data)

def mock_get_movie_details_from_tmdb() -> MoviePublic:
  return MoviePublic(id=123, title="Mock Title", thumbnail_url="https://example.com/thumbnail.png")

@pytest.fixture(scope="module")
async def test_client():

  app.dependency_overrides[get_movie_df] = mock_get_movie_df
  app.dependency_overrides[get_movie_details_from_tmdb] = mock_get_movie_details_from_tmdb

  async with LifespanManager(app):
    async with httpx.AsyncClient(app=app, base_url="http://test") as test_client:
      yield test_client
