import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test /health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_upload_page(client):
    """Test upload page loads"""
    response = client.get("/upload")
    assert response.status_code == 200
    assert b"Upload Image" in response.data
