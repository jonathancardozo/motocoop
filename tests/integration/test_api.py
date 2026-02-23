"""
Test da API principal
"""
import pytest
from fastapi.testclient import TestClient

from src.presentation.api.main import app


@pytest.fixture
def client():
    """Fixture do cliente de teste"""
    return TestClient(app)


def test_root_endpoint(client):
    """Testa o endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["service"] == "MotoCoop API"


def test_health_check(client):
    """Testa o health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
