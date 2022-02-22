from httpx import AsyncClient, codes
import pytest

@pytest.mark.asyncio
async def test_create_user(test_client: AsyncClient):
  response = await test_client.post("/users")
  assert response.status_code == codes.CREATED

