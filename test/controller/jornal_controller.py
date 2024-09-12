from fastapi.testclient import TestClient
from main import app
from src.repository.jornal_repository import JornalRepository
from src.schemes.jornal import JornalOut
from unittest.mock import patch
import pytest

client = TestClient(app)

# Mock data for testing
test_jornal_data = [
    {"id": 1, "title": "Test Jornal 1", "content": "Content of test jornal 1"},
    {"id": 2, "title": "Test Jornal 2", "content": "Content of test jornal 2"}
]

# Convert mock data to JornalOut objects
test_jornal_objects = [JornalOut(**jornal) for jornal in test_jornal_data]

@pytest.fixture
def mock_jornal_repository_get_all():
    with patch.object(JornalRepository, 'get_all', return_value=test_jornal_objects) as mock:
        yield mock

@pytest.fixture
def mock_jornal_repository_get_by_id():
    with patch.object(JornalRepository, 'get_by_id', side_effect=lambda id: next((jornal for jornal in test_jornal_objects if jornal.id == id), None)) as mock:
        yield mock

@pytest.fixture
def mock_jornal_repository_create():
    with patch.object(JornalRepository, 'create', side_effect=lambda jornal: test_jornal_objects.append(jornal)) as mock:
        yield mock

@pytest.fixture
def mock_jornal_repository_update():
    with patch.object(JornalRepository, 'update', side_effect=lambda jornal: test_jornal_objects.append(jornal)) as mock:
        yield mock

def test_get_jornals_shouldReturnAllJornals(mock_jornal_repository_get_all):
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json()) == len(test_jornal_data)
    assert response.json() == test_jornal_data

def test_get_jornal_shouldReturnJornalById(mock_jornal_repository_get_by_id):
    test_id = 1
    response = client.get(f"/{test_id}")
    assert response.status_code == 200
    assert response.json() == test_jornal_data[0]

def test_create_jornal_shouldCreateJornal(mock_jornal_repository_create):
    new_jornal = {"id": 3, "title": "Test Jornal 3", "content": "Content of test jornal 3"}
    response = client.post("/", json=new_jornal)
    assert response.status_code == 201
    assert response.json() == new_jornal
    assert len(test_jornal_objects) == 3

def test_update_jornal_shouldUpdateJornal(mock_jornal_repository_update):
    updated_jornal = {"id": 1, "title": "Updated Test Jornal 1", "content": "Updated content of test jornal 1"}
    response = client.put("/", json=updated_jornal)
    assert response.status_code == 200
    assert response.json() == updated_jornal
    assert any(jornal.title == "Updated Test Jornal 1" for jornal in test_jornal_objects)