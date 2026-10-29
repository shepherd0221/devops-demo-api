
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello, DevOps!"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_item():
    response = client.get("/items/123")

    assert response.status_code == 200
    assert response.json()["item_id"] == 123


def test_invalid_item_id():
    response = client.get("/items/abc")

    assert response.status_code == 422


def example():
    unused_variable = 123
    return "hello"