# See: https://docs.pytest.org/en/latest/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

import asyncio
import httpx
import pytest
from asgi_lifespan import LifespanManager

# Override configuration variables for tests
import os

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

@pytest.fixture(scope="module")
async def test_client():
  async with LifespanManager(app):
    async with httpx.AsyncClient(app=app, base_url="http://test") as test_client:
      yield test_client
