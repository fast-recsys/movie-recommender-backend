import pytest
from httpx import AsyncClient, codes

@pytest.mark.asyncio
async def test_root(test_client: AsyncClient):
  response = await test_client.get("/")
  assert response.status_code == codes.OK
