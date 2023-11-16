# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_form():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text

def test_create_greeting():
    response = client.post("/", data={"name": "John Doe"})
    assert response.status_code == 200
    assert "Hello, John Doe!" in response.text
