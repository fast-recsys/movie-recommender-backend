from json import JSONEncoder
from typing import List
from httpx import AsyncClient, codes
import pytest
import pandas as pd

from app.main import app
from app.models.movie import MoviePublic
from app.data import get_fetcher_instance, get_movie_details_from_tmdb, get_movie_df, get_unrated_movie_details


def mock_get_movie_df():
  mock_data = {'movieId': [1], 'imdbId': [321], 'tmdbId': [123]}
  return pd.DataFrame(mock_data)

def mock_get_movie_details_from_tmdb() -> MoviePublic:
  return MoviePublic(id=123, title="Mock Title", thumbnail_url="https://example.com/thumbnail.png")

def get_unrated_movie_details() -> List[MoviePublic]:
  return [MoviePublic(id=123, title="Mock Title", thumbnail_url="https://example.com/thumbnail.png")]

class MockMovieFetcher:
  async def __call__(self, _: int):
    return mock_get_movie_details_from_tmdb()

def get_mock_movie_fetcher():
  return MockMovieFetcher()


@pytest.fixture(scope="module")
async def mock_user_id(test_client: AsyncClient):
  response = await test_client.post("/users")
  response_json = response.json()
  yield response_json["_id"]


@pytest.mark.asyncio
async def test_get_unrated_movies(mock_user_id: str, test_client: AsyncClient):

  app.dependency_overrides[get_movie_details_from_tmdb] = mock_get_movie_details_from_tmdb
  app.dependency_overrides[get_fetcher_instance] = get_mock_movie_fetcher

  response = await test_client.get(f"/users/{mock_user_id}/unrated")
  assert response.status_code == codes.OK


@pytest.mark.asyncio
async def test_save_movie_ratings(mock_user_id: str, test_client: AsyncClient):
  response = await test_client.get(f"users/{mock_user_id}/ratings")
  assert response.status_code == codes.OK

  response_json = response.json()

  assert 'ratings' in response_json

  previous_ratings_count = len(response_json['ratings'])

  payload = {'ratings': [{'movie_id': 1, 'rating': 5}, {'movie_id': 2, 'rating': 3}]}
  response = await test_client.post(f"users/{mock_user_id}/ratings", content=JSONEncoder().encode(payload))
  assert response.status_code == codes.NO_CONTENT

  response = await test_client.get(f"users/{mock_user_id}/ratings")
  assert response.status_code == codes.OK
  response_json = response.json()

  current_ratings_count = len(response_json['ratings'])

  assert current_ratings_count == previous_ratings_count + 2


@pytest.mark.asyncio
async def test_recommendations(mock_user_id: str, test_client: AsyncClient):
  app.dependency_overrides[get_fetcher_instance] = get_mock_movie_fetcher
  response = await test_client.get(f"users/{mock_user_id}/recommendations")
  assert response.status_code == codes.OK


