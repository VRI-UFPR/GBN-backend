from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in a file named main.py
from src.schemes.texto_ocr import TextoOcrOut
from src.repository.texto_ocr_repository import TextoOcrRepository
import pytest
from unittest.mock import MagicMock

# Mocking the TextoOcrRepository for isolation
@pytest.fixture
def mock_texto_ocr_repository(monkeypatch):
    mock_repo = MagicMock(TextoOcrRepository)
    monkeypatch.setattr("src.repository.texto_ocr_repository.TextoOcrRepository", mock_repo)
    return mock_repo

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_get_all_texto_ocr_should_return_200(mock_texto_ocr_repository, client):
    mock_texto_ocr_repository.get_all.return_value = []
    response = client.get("/")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert isinstance(response.json(), list), "Expected response to be a list"

def test_get_texto_ocr_by_id_should_return_200_if_found(mock_texto_ocr_repository, client):
    mock_texto_ocr_repository.get_by_id.return_value = TextoOcrOut()
    response = client.get("/1")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert isinstance(response.json(), dict), "Expected response to be a dictionary"

def test_get_texto_ocr_by_id_should_return_none_if_not_found(mock_texto_ocr_repository, client):
    mock_texto_ocr_repository.get_by_id.return_value = None
    response = client.get("/999")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() is None, "Expected response to be None for non-existing ID"

def test_get_texto_ocr_by_pagina_id_should_return_200_if_found(mock_texto_ocr_repository, client):
    mock_texto_ocr_repository.get_by_pagina_id.return_value = TextoOcrOut()
    response = client.get("/pagina/1")
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert isinstance(response.json(), dict), "Expected response to be a dictionary"

def test_create_texto_ocr_should_return_201(mock_texto_ocr_repository, client):
    sample_texto_ocr = {"id": 1, "content": "Sample OCR content"}
    mock_texto_ocr_repository.create.return_value = TextoOcrOut(**sample_texto_ocr)
    response = client.post("/", json=sample_texto_ocr)
    assert response.status_code == 201, "Expected status code to be 201 Created"
    assert response.json() == sample_texto_ocr, "Expected response to match the created TextoOcr"

def test_update_texto_ocr_should_return_200(mock_texto_ocr_repository, client):
    updated_texto_ocr = {"id": 1, "content": "Updated OCR content"}
    mock_texto_ocr_repository.update.return_value = TextoOcrOut(**updated_texto_ocr)
    response = client.put("/", json=updated_texto_ocr)
    assert response.status_code == 200, "Expected status code to be 200 OK"
    assert response.json() == updated_texto_ocr, "Expected response to match the updated TextoOcr"