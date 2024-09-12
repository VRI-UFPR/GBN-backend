from fastapi.testclient import TestClient
from main import app
from src.schemes.pontuacao import PontuacaoOut, PontuacaoCreate
from unittest.mock import patch

client = TestClient(app)

def test_get_pontuacao_should_return_200():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.get_all') as mock_get_all:
        mock_get_all.return_value = [PontuacaoOut(id=1, score=100)]
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == [{"id": 1, "score": 100}], "Should return a list of pontuacao"

def test_get_pontuacao_top10_should_return_200():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.get_top10') as mock_get_top10:
        mock_get_top10.return_value = [PontuacaoOut(id=1, score=100)]
        response = client.get("/top10")
        assert response.status_code == 200
        assert response.json() == [{"id": 1, "score": 100}], "Should return top 10 pontuacao"

def test_get_pontuacao_by_id_should_return_200():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.get_by_id') as mock_get_by_id:
        mock_get_by_id.return_value = PontuacaoOut(id=1, score=100)
        response = client.get("/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "score": 100}, "Should return pontuacao by id"

def test_create_pontuacao_should_return_201():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.create') as mock_create:
        test_pontuacao = {"id": 1, "score": 100}
        mock_create.return_value = test_pontuacao
        response = client.post("/", json=test_pontuacao)
        assert response.status_code == 201
        assert response.json() == test_pontuacao, "Should create and return pontuacao"

def test_update_pontuacao_should_return_200():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.update') as mock_update:
        test_pontuacao = {"id": 1, "score": 150}
        mock_update.return_value = test_pontuacao
        response = client.put("/", json=test_pontuacao)
        assert response.status_code == 200
        assert response.json() == test_pontuacao, "Should update and return pontuacao"

# Additional test cases to cover error handling and edge cases
def test_get_pontuacao_by_invalid_id_should_return_404():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.get_by_id') as mock_get_by_id:
        mock_get_by_id.return_value = None
        response = client.get("/999")
        assert response.status_code == 404, "Should return 404 for non-existing id"

def test_create_pontuacao_with_invalid_data_should_return_422():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.create') as mock_create:
        invalid_pontuacao = {"id": "not_an_int", "score": "not_an_int"}
        response = client.post("/", json=invalid_pontuacao)
        assert response.status_code == 422, "Should return 422 for invalid data"

def test_update_pontuacao_with_invalid_data_should_return_422():
    with patch('src.repository.pontuacao_repository.PontuacaoRepository.update') as mock_update:
        invalid_pontuacao = {"id": "not_an_int", "score": "not_an_int"}
        response = client.put("/", json=invalid_pontuacao)
        assert response.status_code == 422, "Should return 422 for invalid data"