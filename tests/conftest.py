# See: https://docs.pytest.org/en/latest/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

import asyncio
import httpx
import pytest
from asgi_lifespan import LifespanManager

from app.main import app

@pytest.fixture(scope="session")
def event_loop():
  loop = asyncio.get_event_loop()
  yield loop
  loop.close()

@pytest.fixture
async def test_client():
  async with LifespanManager(app):
    async with httpx.AsyncClient(app=app, base_url="http://test") as test_client:
      yield test_client
