# Get movie details endpoint
# Mock: data frame with id and tmdbId
#       get_movie_details_from_tmdb response (MoviePublic instance)

from app.data import get_movie_details_from_tmdb, get_movie_df
from app.main import app

from httpx import AsyncClient, codes
import pytest

from tests.conftest import mock_get_movie_details_from_tmdb, mock_get_movie_df

@pytest.mark.asyncio
async def test_get_known_movie_details(test_client: AsyncClient):

  app.dependency_overrides[get_movie_df] = mock_get_movie_df
  app.dependency_overrides[get_movie_details_from_tmdb] = mock_get_movie_details_from_tmdb

  response = await test_client.get(f"/movies/1")

  assert response.status_code == codes.OK

  response_json = response.json()

  assert response_json["id"] == 1
  assert response_json["title"] == "Mock Title"
  assert response_json["thumbnail_url"] == "https://example.com/thumbnail.png"

  app.dependency_overrides = {}

@pytest.mark.asyncio
async def test_get_unknown_movie_details(test_client: AsyncClient):

  app.dependency_overrides[get_movie_df] = mock_get_movie_df

  response = await test_client.get(f"/movies/2")

  assert response.status_code == codes.NOT_FOUND

  app.dependency_overrides = {}
