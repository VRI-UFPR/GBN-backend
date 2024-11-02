from fastapi.testclient import TestClient
from main import app
from src.repository.pagina_repository import PaginaRepository
from src.schemes.pagina import PaginaOut
from unittest.mock import MagicMock
import pytest

client = TestClient(app)

# Mocking PaginaRepository for isolation
PaginaRepository.get_all = MagicMock(return_value=[PaginaOut(id=1, title="Test Page", content="Test Content")])
PaginaRepository.get_by_id = MagicMock(return_value=PaginaOut(id=1, title="Test Page", content="Test Content"))
PaginaRepository.create = MagicMock(return_value=PaginaOut(id=1, title="Test Page", content="Test Content"))
PaginaRepository.update = MagicMock(return_value=PaginaOut(id=1, title="Test Page Updated", content="Test Content Updated"))

@pytest.fixture
def mock_pagina():
    return PaginaOut(id=1, title="Test Page", content="Test Content")

def test_get_all_paginas_should_return_200():
    response = client.get("/")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() == [{"id": 1, "title": "Test Page", "content": "Test Content"}], "Expected JSON response to match mock data"

def test_get_pagina_unica_should_return_200():
    response = client.get("/pagina_unica")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() == {"id": 1, "title": "Test Page", "content": "Test Content"}, "Expected JSON response to match mock data"

def test_get_pagina_by_id_should_return_200(mock_pagina):
    response = client.get(f"/{mock_pagina.id}")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() == {"id": mock_pagina.id, "title": mock_pagina.title, "content": mock_pagina.content}, "Expected JSON response to match mock data"

def test_create_pagina_should_return_201(mock_pagina):
    response = client.post("/", json=mock_pagina.dict())
    assert response.status_code == 201, "Expected status code to be 201 Created"
    assert response.json() == mock_pagina.dict(), "Expected JSON response to match mock data"

def test_update_pagina_should_return_200(mock_pagina):
    updated_pagina = mock_pagina.dict()
    updated_pagina["title"] = "Test Page Updated"
    updated_pagina["content"] = "Test Content Updated"
    response = client.put("/", json=updated_pagina)
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() == updated_pagina, "Expected JSON response to match updated mock data"