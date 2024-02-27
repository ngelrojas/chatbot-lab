import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_chat_bot(client):
    response = client.post("/chat", json={"prompt": "Test prompt"})
    assert response.status_code == 200
