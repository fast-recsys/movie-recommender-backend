# Get movie details endpoint
# Mock: data frame with id and tmdbId
#       get_movie_details_from_tmdb response (MoviePublic instance)


from httpx import AsyncClient, codes
import pytest



@pytest.mark.asyncio
async def test_get_known_movie_details(test_client: AsyncClient):

  response = await test_client.get(f"/movies/1")

  print(response.json())

  assert response.status_code == codes.OK

  response_json = response.json()

  assert response_json["id"] == 1
  assert response_json["title"] == "Mock Title"
  assert response_json["thumbnail_url"] == "https://example.com/thumbnail.png"
