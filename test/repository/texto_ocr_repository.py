from unittest.mock import MagicMock
import pytest

from src.repository.base_repository import BaseRepository
from src.models.texto_ocr import TextoOcr
from src.repository.texto_ocr_repository import TextoOcrRepository

@pytest.fixture
def base_repository_mock():
    base_repository = BaseRepository(TextoOcr)
    base_repository.get_all = MagicMock(return_value=[TextoOcr(id=1, pagina_id=1, content="Sample Text")])
    base_repository.get_by_id = MagicMock(return_value=TextoOcr(id=1, pagina_id=1, content="Sample Text"))
    base_repository.get_by_column = MagicMock(return_value=[TextoOcr(id=1, pagina_id=1, content="Sample Text")])
    base_repository.create = MagicMock(return_value=TextoOcr(id=1, pagina_id=1, content="Sample Text"))
    base_repository.update = MagicMock(return_value=TextoOcr(id=1, pagina_id=1, content="Sample Text"))
    return base_repository

@pytest.fixture
def texto_ocr_repository(base_repository_mock):
    texto_ocr_repository = TextoOcrRepository()
    texto_ocr_repository.base_repository = base_repository_mock
    return texto_ocr_repository

def test_get_all_should_return_list_of_texto_ocr(texto_ocr_repository):
    result = texto_ocr_repository.get_all()
    assert isinstance(result, list), "Expected result to be a list"
    assert len(result) > 0, "Expected non-empty list"
    assert isinstance(result[0], TextoOcr), "Expected list elements to be instances of TextoOcr"

def test_get_by_id_should_return_texto_ocr_instance(texto_ocr_repository):
    result = texto_ocr_repository.get_by_id(1)
    assert isinstance(result, TextoOcr), "Expected result to be an instance of TextoOcr"

def test_get_by_pagina_id_should_return_list_of_texto_ocr(texto_ocr_repository):
    result = texto_ocr_repository.get_by_pagina_id(1)
    assert isinstance(result, list), "Expected result to be a list"
    assert len(result) > 0, "Expected non-empty list"
    assert isinstance(result[0], TextoOcr), "Expected list elements to be instances of TextoOcr"

def test_create_should_return_texto_ocr_instance(texto_ocr_repository):
    sample_texto_ocr = TextoOcr(id=1, pagina_id=1, content="Sample Text")
    result = texto_ocr_repository.create(sample_texto_ocr)
    assert isinstance(result, TextoOcr), "Expected result to be an instance of TextoOcr"

def test_update_should_return_updated_texto_ocr_instance(texto_ocr_repository):
    sample_texto_ocr = TextoOcr(id=1, pagina_id=1, content="Updated Text")
    result = texto_ocr_repository.update(sample_texto_ocr)
    assert isinstance(result, TextoOcr), "Expected result to be an instance of TextoOcr"
    assert result.content == "Updated Text", "Expected content to be updated"