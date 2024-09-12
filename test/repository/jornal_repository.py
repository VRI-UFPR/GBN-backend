```python
import pytest
from unittest.mock import MagicMock
from src.repository.jornal_repository import JornalRepository
from src.models.jornal import Jornal

@pytest.fixture
def mock_base_repository():
    mock = MagicMock()
    mock.get_all.return_value = []
    mock.get_by_id.return_value = None
    mock.create.return_value = Jornal(id=1, title="Test Jornal", content="Test Content")
    mock.update.return_value = Jornal(id=1, title="Updated Jornal", content="Updated Content")
    return mock

@pytest.fixture
def jornal_repository(mock_base_repository):
    repository = JornalRepository()
    repository.base_repository = mock_base_repository
    return repository

def test_get_all_should_return_empty_list(jornal_repository):
    result = jornal_repository.get_all()
    assert isinstance(result, list), "Expected result to be a list"
    assert len(result) == 0, "Expected empty list"

def test_get_by_id_with_nonexistent_id_should_return_none(jornal_repository):
    result = jornal_repository.get_by_id(999)
    assert result is None, "Expected None for nonexistent ID"

def test_create_should_return_jornal_object(jornal_repository):
    jornal_data = {"title": "Test Jornal", "content": "Test Content"}
    jornal = Jornal(**jornal_data)
    result = jornal_repository.create(jornal)
    assert isinstance(result, Jornal), "Expected result to be a Jornal object"
    assert result.title == "Test Jornal", "Expected title to match input data"
    assert result.content == "Test Content", "Expected content to match input data"

def test_update_should_log_and_return_updated_jornal(jornal_repository, caplog):
    jornal_data = {"title": "Updated Jornal", "content": "Updated Content"}
    jornal = Jornal(**jornal_data)
    with caplog.at_level(logging.INFO):
        result = jornal_repository.update(jornal)
    assert "Updating jornal" in caplog.text, "Expected update action to be logged"
    assert isinstance(result, Jornal), "Expected result to be a Jornal object"
    assert result.title == "Updated Jornal", "Expected title to be updated"
    assert result.content == "Updated Content", "Expected content to be updated"
```