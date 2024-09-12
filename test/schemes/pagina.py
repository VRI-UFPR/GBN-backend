import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError

# Assuming the provided code is in a file named models.py
from models import PaginaCreate, PaginaInDatabase, PaginaOut

def test_PaginaCreate_WithValidData_ShouldCreateSuccessfully():
    data = {
        "pagina_index": 1,
        "image_path": "path/to/image.jpg",
        "iiif_path": "path/to/iiif",
        "fontes": "Fonte 1"
    }
    pagina = PaginaCreate(**data)
    assert pagina.pagina_index == data["pagina_index"], "pagina_index should match the input data"
    assert pagina.image_path == data["image_path"], "image_path should match the input data"
    assert pagina.iiif_path == data["iiif_path"], "iiif_path should match the input data"
    assert pagina.fontes == data["fontes"], "fontes should match the input data"

def test_PaginaInDatabase_WithValidData_ShouldCreateSuccessfully():
    data = {
        "pagina_index": 1,
        "image_path": "path/to/image.jpg",
        "iiif_path": "path/to/iiif",
        "fontes": "Fonte 1",
        "exemplar_id": 123
    }
    pagina = PaginaInDatabase(**data)
    assert pagina.pagina_index == data["pagina_index"], "pagina_index should match the input data"
    assert pagina.image_path == data["image_path"], "image_path should match the input data"
    assert pagina.iiif_path == data["iiif_path"], "iiif_path should match the input data"
    assert pagina.fontes == data["fontes"], "fontes should match the input data"
    assert pagina.exemplar_id == data["exemplar_id"], "exemplar_id should match the input data"
    assert isinstance(pagina.created_at, datetime), "created_at should be a datetime instance"
    assert isinstance(pagina.updated_at, datetime), "updated_at should be a datetime instance"

def test_PaginaOut_WithValidData_ShouldCreateSuccessfully():
    data = {
        "id": 1,
        "pagina_index": 1,
        "image_path": "path/to/image.jpg",
        "iiif_path": "path/to/iiif",
        "fontes": "Fonte 1",
        "exemplar_id": 123
    }
    pagina = PaginaOut(**data)
    assert pagina.id == data["id"], "id should match the input data"
    assert pagina.pagina_index == data["pagina_index"], "pagina_index should match the input data"
    assert pagina.image_path == data["image_path"], "image_path should match the input data"
    assert pagina.iiif_path == data["iiif_path"], "iiif_path should match the input data"
    assert pagina.fontes == data["fontes"], "fontes should match the input data"
    assert pagina.exemplar_id == data["exemplar_id"], "exemplar_id should match the input data"

def test_PaginaInDatabase_WithFutureDates_ShouldRaiseValidationError():
    data = {
        "pagina_index": 1,
        "image_path": "path/to/image.jpg",
        "iiif_path": "path/to/iiif",
        "fontes": "Fonte 1",
        "exemplar_id": 123,
        "created_at": datetime.now() + timedelta(days=1),  # Future date
        "updated_at": datetime.now() + timedelta(days=1)   # Future date
    }
    with pytest.raises(ValidationError) as exc_info:
        PaginaInDatabase(**data)
    assert "cannot be in the future" in str(exc_info.value), "Should raise a validation error for future dates"

def test_PaginaCreate_WithMissingRequiredFields_ShouldRaiseValidationError():
    data = {
        # "pagina_index": 1,  # Missing required field
        "image_path": "path/to/image.jpg",
        "iiif_path": "path/to/iiif",
        "fontes": "Fonte 1"
    }
    with pytest.raises(ValidationError) as exc_info:
        PaginaCreate(**data)
    assert "field required" in str(exc_info.value), "Should raise a validation error for missing required fields"