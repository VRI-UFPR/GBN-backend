```python
import pytest
from unittest.mock import MagicMock
from src.repository.base_repository import BaseRepository
from src.models.texto_correcao_manual import TextoCorrecaoManual
from src.repository.texto_correcao_manual_repository import TextoCorrecaoManualRepository

@pytest.fixture
def base_repository_mock():
    base_repository = BaseRepository(TextoCorrecaoManual)
    base_repository.get_all = MagicMock(return_value=[])
    base_repository.get_by_id = MagicMock()
    base_repository.create = MagicMock()
    base_repository.update = MagicMock()
    return base_repository

@pytest.fixture
def texto_correcao_manual_repository(base_repository_mock):
    repository = TextoCorrecaoManualRepository()
    repository.base_repository = base_repository_mock
    return repository

def test_get_all_should_return_empty_list(texto_correcao_manual_repository):
    result = texto_correcao_manual_repository.get_all()
    assert result == [], "Expected an empty list when no records are present"

def test_get_by_id_should_call_base_repository_with_correct_id(texto_correcao_manual_repository, base_repository_mock):
    test_id = 1
    texto_correcao_manual_repository.get_by_id(test_id)
    base_repository_mock.get_by_id.assert_called_once_with(test_id)

def test_create_should_call_base_repository_create_with_correct_object(texto_correcao_manual_repository, base_repository_mock):
    test_data = {"id": 1, "content": "Test content"}
    texto_correcao_manual = TextoCorrecaoManual(**test_data)
    texto_correcao_manual_repository.create(texto_correcao_manual)
    base_repository_mock.create.assert_called_once_with(texto_correcao_manual)

def test_update_should_call_base_repository_update_with_correct_object(texto_correcao_manual_repository, base_repository_mock):
    test_data = {"id": 1, "content": "Updated content"}
    texto_correcao_manual = TextoCorrecaoManual(**test_data)
    texto_correcao_manual_repository.update(texto_correcao_manual)
    base_repository_mock.update.assert_called_once_with(texto_correcao_manual)
```