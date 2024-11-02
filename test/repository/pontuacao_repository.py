```python
import pytest
from unittest.mock import MagicMock
from src.repository.base_repository import BaseRepository
from src.models.pontuacao import Pontuacao
from src.repository.pontuacao_repository import PontuacaoRepository

@pytest.fixture
def mock_base_repository():
    base_repository = MagicMock(spec=BaseRepository)
    return base_repository

@pytest.fixture
def pontuacao_repository(mock_base_repository):
    PontuacaoRepository.pontuacao_repository = mock_base_repository
    return PontuacaoRepository()

def test_get_all_should_return_all_pontuacoes(pontuacao_repository, mock_base_repository):
    mock_base_repository.get_all.return_value = [Pontuacao(id=1, pontuacao=100), Pontuacao(id=2, pontuacao=200)]
    result = pontuacao_repository.get_all()
    assert len(result) == 2, "Should return all pontuacoes"
    mock_base_repository.get_all.assert_called_once()

def test_get_top10_should_return_top_10_pontuacoes(pontuacao_repository, mock_base_repository):
    mock_base_repository.get_all.return_value = [Pontuacao(id=i, pontuacao=i*10) for i in range(1, 21)]
    result = pontuacao_repository.get_top10()
    assert len(result) == 10, "Should return top 10 pontuacoes"
    assert result[0].pontuacao == 200, "Highest score should be first"
    mock_base_repository.get_all.assert_called_once()

def test_get_by_id_should_return_correct_pontuacao(pontuacao_repository, mock_base_repository):
    mock_base_repository.get_by_id.return_value = Pontuacao(id=1, pontuacao=100)
    result = pontuacao_repository.get_by_id(1)
    assert result.id == 1, "Should return the pontuacao with correct id"
    mock_base_repository.get_by_id.assert_called_once_with(1)

def test_create_should_call_create_on_base_repository(pontuacao_repository, mock_base_repository):
    pontuacao_data = {"id": 1, "pontuacao": 100}
    pontuacao_repository.create(Pontuacao(**pontuacao_data))
    mock_base_repository.create.assert_called_once()
    assert isinstance(mock_base_repository.create.call_args[0][0], Pontuacao), "Should create a Pontuacao object"

def test_update_should_call_update_on_base_repository(pontuacao_repository, mock_base_repository):
    pontuacao_data = {"id": 1, "pontuacao": 200}
    pontuacao_repository.update(Pontuacao(**pontuacao_data))
    mock_base_repository.update.assert_called_once()
    assert isinstance(mock_base_repository.update.call_args[0][0], Pontuacao), "Should update a Pontuacao object"
```