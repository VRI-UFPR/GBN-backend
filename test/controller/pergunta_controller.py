from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in a file named main.py
from src.schemes.pergunta import PerguntaOut
from unittest.mock import patch

client = TestClient(app)

def test_get_pergunta_should_return_200():
    with patch('src.repository.pergunta_repository.PerguntaRepository.get_all') as mock_get_all:
        mock_get_all.return_value = [PerguntaOut(id=1, titulo="Sample Question", descricao="This is a sample question")]
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == [{"id": 1, "titulo": "Sample Question", "descricao": "This is a sample question"}], "Response does not match expected JSON structure or data"

def test_get_pergunta_by_pagina_should_return_200():
    with patch('src.repository.pergunta_repository.PerguntaRepository.get_by_pagina_id') as mock_get_by_pagina_id:
        mock_get_by_pagina_id.return_value = PerguntaOut(id=1, titulo="Sample Question", descricao="This is a sample question")
        response = client.get("/pagina/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "titulo": "Sample Question", "descricao": "This is a sample question"}, "Response does not match expected JSON structure or data"

def test_get_pergunta_by_id_should_return_200():
    with patch('src.repository.pergunta_repository.PerguntaRepository.get_by_id') as mock_get_by_id:
        mock_get_by_id.return_value = PerguntaOut(id=1, titulo="Sample Question", descricao="This is a sample question")
        response = client.get("/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "titulo": "Sample Question", "descricao": "This is a sample question"}, "Response does not match expected JSON structure or data"

def test_create_pergunta_should_return_201():
    with patch('src.repository.pergunta_repository.PerguntaRepository.create') as mock_create:
        mock_create.return_value = None  # Assuming create method returns None
        pergunta = {"titulo": "New Question", "descricao": "This is a new question"}
        response = client.post("/", json=pergunta)
        assert response.status_code == 201
        assert response.json() == pergunta, "Response does not match expected JSON structure or data"

def test_update_pergunta_should_return_200():
    with patch('src.repository.pergunta_repository.PerguntaRepository.update') as mock_update:
        mock_update.return_value = None  # Assuming update method returns None
        pergunta = {"id": 1, "titulo": "Updated Question", "descricao": "This question has been updated"}
        response = client.put("/", json=pergunta)
        assert response.status_code == 200
        assert response.json() == pergunta, "Response does not match expected JSON structure or data"