from unittest.mock import MagicMock
import pytest

from src.repository.base_repository import BaseRepository
from src.models.alternativa import Alternativa
from src.repository.alternativa_repository import AlternativaRepository

@pytest.fixture
def base_repository_mock():
    base_repository = BaseRepository(Alternativa)
    base_repository.get_all = MagicMock(return_value=[Alternativa(id=1, pergunta_id=1, texto='Alternativa 1', correta=False)])
    base_repository.get_by_id = MagicMock(return_value=Alternativa(id=1, pergunta_id=1, texto='Alternativa 1', correta=False))
    base_repository.get_by_column = MagicMock(return_value=[Alternativa(id=1, pergunta_id=1, texto='Alternativa 1', correta=False)])
    base_repository.create = MagicMock(return_value=Alternativa(id=1, pergunta_id=1, texto='Nova Alternativa', correta=True))
    base_repository.update = MagicMock(return_value=Alternativa(id=1, pergunta_id=1, texto='Alternativa Atualizada', correta=True))
    return base_repository

@pytest.fixture
def alternativa_repository(base_repository_mock):
    alternativa_repository = AlternativaRepository()
    alternativa_repository.base_repository = base_repository_mock
    return alternativa_repository

def test_get_all_should_return_list_of_alternativas(alternativa_repository):
    alternativas = alternativa_repository.get_all()
    assert isinstance(alternativas, list), "Expected a list of Alternativas"
    assert len(alternativas) > 0, "Expected non-empty list of Alternativas"
    assert isinstance(alternativas[0], Alternativa), "Expected list elements to be instances of Alternativa"

def test_get_by_id_should_return_alternativa(alternativa_repository):
    alternativa = alternativa_repository.get_by_id(1)
    assert isinstance(alternativa, Alternativa), "Expected an instance of Alternativa"
    assert alternativa.id == 1, "Expected Alternativa with ID 1"

def test_get_by_pergunta_id_should_return_list_of_alternativas(alternativa_repository):
    alternativas = alternativa_repository.get_by_pergunta_id(1)
    assert isinstance(alternativas, list), "Expected a list of Alternativas"
    assert len(alternativas) > 0, "Expected non-empty list of Alternativas"
    assert alternativas[0].pergunta_id == 1, "Expected Alternativas with pergunta_id 1"

def test_create_should_return_new_alternativa(alternativa_repository):
    new_alternativa = {"texto": "Nova Alternativa", "correta": True, "pergunta_id": 1}
    created_alternativa = alternativa_repository.create(Alternativa(**new_alternativa))
    assert isinstance(created_alternativa, Alternativa), "Expected an instance of Alternativa"
    assert created_alternativa.texto == "Nova Alternativa", "Expected Alternativa with specified text"
    assert created_alternativa.correta is True, "Expected Alternativa to be marked as correct"

def test_update_should_return_updated_alternativa(alternativa_repository):
    updated_alternativa = {"id": 1, "texto": "Alternativa Atualizada", "correta": True, "pergunta_id": 1}
    result = alternativa_repository.update(Alternativa(**updated_alternativa))
    assert isinstance(result, Alternativa), "Expected an instance of Alternativa"
    assert result.texto == "Alternativa Atualizada", "Expected Alternativa with updated text"
    assert result.correta is True, "Expected Alternativa to be marked as correct after update"