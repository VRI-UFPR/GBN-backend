```python
import pytest
from unittest.mock import MagicMock
from src.repository.base_repository import BaseRepository
from src.models.pagina import Pagina
from src.repository.pagina_repository import PaginaRepository

@pytest.fixture
def pagina_data():
    return {"id": 1, "title": "Test Page", "content": "This is a test page"}

@pytest.fixture
def pagina_repository():
    repository = PaginaRepository()
    repository.base_repository = MagicMock(spec=BaseRepository)
    return repository

def test_get_all_should_return_list_of_paginas(pagina_repository):
    expected_paginas = [Pagina(id=1, title="Page 1", content="Content 1"), Pagina(id=2, title="Page 2", content="Content 2")]
    pagina_repository.base_repository.get_all.return_value = expected_paginas

    paginas = pagina_repository.get_all()

    assert paginas == expected_paginas, "get_all should return a list of Pagina objects"

def test_get_by_id_should_return_pagina_with_specified_id(pagina_repository, pagina_data):
    expected_pagina = Pagina(**pagina_data)
    pagina_repository.base_repository.get_by_id.return_value = expected_pagina

    pagina = pagina_repository.get_by_id(pagina_data["id"])

    assert pagina == expected_pagina, "get_by_id should return the Pagina object with the specified ID"

def test_create_should_add_new_pagina_and_return_it(pagina_repository, pagina_data):
    new_pagina = Pagina(**pagina_data)
    pagina_repository.base_repository.create.return_value = new_pagina

    created_pagina = pagina_repository.create(new_pagina)

    pagina_repository.base_repository.create.assert_called_once_with(new_pagina)
    assert created_pagina == new_pagina, "create should add a new Pagina and return it"

def test_update_should_modify_existing_pagina_and_return_it(pagina_repository, pagina_data):
    updated_pagina_data = pagina_data.copy()
    updated_pagina_data["title"] = "Updated Title"
    updated_pagina = Pagina(**updated_pagina_data)
    pagina_repository.base_repository.update.return_value = updated_pagina

    result_pagina = pagina_repository.update(updated_pagina)

    pagina_repository.base_repository.update.assert_called_once_with(updated_pagina)
    assert result_pagina == updated_pagina, "update should modify the existing Pagina and return it"
```