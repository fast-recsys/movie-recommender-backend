from httpx import AsyncClient, codes
import pytest

@pytest.mark.asyncio
async def test_create_user(test_client: AsyncClient):
  response = await test_client.post("/users")
  assert response.status_code == codes.CREATED


@pytest.fixture(scope="module")
async def mock_user_id(test_client: AsyncClient):
  response = await test_client.post("/users")
  response_json = response.json()
  yield response_json["_id"]

@pytest.mark.asyncio
class TestUserDetails:

  async def test_user_details(self, mock_user_id: str, test_client: AsyncClient):
    response = await test_client.get(f"/users/{mock_user_id}")
    assert response.status_code == codes.OK

  async def test_invalid_user_details(self, test_client: AsyncClient):
    response = await test_client.get(f"/users/11111")
    assert response.status_code == codes.NOT_FOUND
