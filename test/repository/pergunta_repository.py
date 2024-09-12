from unittest.mock import MagicMock
import pytest

from src.repository.base_repository import BaseRepository
from src.models.pergunta import Pergunta
from src.repository.pergunta_repository import PerguntaRepository

@pytest.fixture
def base_repository_mock():
    base_repository = BaseRepository(Pergunta)
    base_repository.get_all = MagicMock(return_value=[Pergunta(id=1, pagina_id=1), Pergunta(id=2, pagina_id=2)])
    base_repository.get_by_id = MagicMock(return_value=Pergunta(id=1, pagina_id=1))
    base_repository.get_by_column = MagicMock(return_value=[Pergunta(id=1, pagina_id=1)])
    base_repository.create = MagicMock(return_value=Pergunta(id=3, pagina_id=3))
    base_repository.update = MagicMock(return_value=Pergunta(id=1, pagina_id=1, texto="Updated"))
    return base_repository

@pytest.fixture
def pergunta_repository(base_repository_mock):
    pergunta_repository = PerguntaRepository()
    pergunta_repository.base_repository = base_repository_mock
    return pergunta_repository

def test_get_all_should_return_all_perguntas(pergunta_repository):
    perguntas = pergunta_repository.get_all()
    assert len(perguntas) == 2, "Should return 2 perguntas"

def test_get_by_id_should_return_correct_pergunta(pergunta_repository):
    pergunta = pergunta_repository.get_by_id(1)
    assert pergunta.id == 1, "Should return the pergunta with ID 1"

def test_get_by_pagina_id_should_return_correct_perguntas(pergunta_repository):
    perguntas = pergunta_repository.get_by_pagina_id(1)
    assert len(perguntas) == 1, "Should return 1 pergunta for pagina_id 1"
    assert perguntas[0].pagina_id == 1, "Should return the pergunta with pagina_id 1"

def test_create_should_create_pergunta(pergunta_repository):
    new_pergunta = Pergunta(id=3, pagina_id=3)
    created_pergunta = pergunta_repository.create(new_pergunta)
    assert created_pergunta.id == 3, "Should create a pergunta with ID 3"

def test_update_should_update_pergunta(pergunta_repository):
    updated_pergunta = Pergunta(id=1, pagina_id=1, texto="Updated")
    result = pergunta_repository.update(updated_pergunta)
    assert result.texto == "Updated", "Should update the pergunta's texto to 'Updated'"

# This test suite focuses on testing the PerguntaRepository class by mocking the BaseRepository's behavior.
# It ensures that each method in PerguntaRepository interacts correctly with the BaseRepository and returns the expected results.