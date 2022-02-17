from app.test_main import client


def test_checkpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == "The server is alive..."
