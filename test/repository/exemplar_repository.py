from unittest.mock import MagicMock
import pytest

from src.repository.base_repository import BaseRepository
from src.models.exemplar import Exemplar
from src.repository.exemplar_repository import ExemplarRepository

@pytest.fixture
def base_repository_mock():
    base_repository = BaseRepository(Exemplar)
    base_repository.get_all = MagicMock(return_value=[Exemplar(id=1, name="Test Exemplar")])
    base_repository.get_by_id = MagicMock(return_value=Exemplar(id=1, name="Test Exemplar"))
    base_repository.create = MagicMock(return_value=Exemplar(id=1, name="Test Exemplar"))
    base_repository.update = MagicMock(return_value=Exemplar(id=1, name="Updated Exemplar"))
    return base_repository

@pytest.fixture
def exemplar_repository(base_repository_mock):
    exemplar_repository = ExemplarRepository()
    exemplar_repository.base_repository = base_repository_mock
    return exemplar_repository

def test_get_all_should_return_list_of_exemplars(exemplar_repository):
    exemplars = exemplar_repository.get_all()
    assert isinstance(exemplars, list), "Expected to get a list of exemplars"
    assert len(exemplars) > 0, "Expected non-empty list of exemplars"
    assert isinstance(exemplars[0], Exemplar), "Expected list elements to be instances of Exemplar"

def test_get_by_id_should_return_exemplar(exemplar_repository):
    exemplar = exemplar_repository.get_by_id(1)
    assert isinstance(exemplar, Exemplar), "Expected to get an instance of Exemplar"
    assert exemplar.id == 1, "Expected to get exemplar with ID 1"

def test_create_should_return_new_exemplar(exemplar_repository):
    new_exemplar = {"id": 2, "name": "New Exemplar"}
    exemplar = exemplar_repository.create(Exemplar(**new_exemplar))
    assert isinstance(exemplar, Exemplar), "Expected to create and return an instance of Exemplar"
    assert exemplar.id == new_exemplar["id"], "Expected created exemplar to have the correct ID"
    assert exemplar.name == new_exemplar["name"], "Expected created exemplar to have the correct name"

def test_update_should_return_updated_exemplar(exemplar_repository):
    updated_exemplar = {"id": 1, "name": "Updated Exemplar"}
    exemplar = exemplar_repository.update(Exemplar(**updated_exemplar))
    assert isinstance(exemplar, Exemplar), "Expected to update and return an instance of Exemplar"
    assert exemplar.id == updated_exemplar["id"], "Expected updated exemplar to have the correct ID"
    assert exemplar.name == updated_exemplar["name"], "Expected updated exemplar to have the correct name"