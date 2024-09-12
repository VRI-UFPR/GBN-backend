```python
import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError
from uuid import uuid4
from pathlib import Path

# Assuming the provided Python code is in a file named models.py
from models import TextoCreate, TextoOcrInDatabase, TextoOcrOut

# Helper function to generate a unique string, useful for testing unique fields
def generate_unique_text(prefix="text"):
    return f"{prefix}_{uuid4()}"

# Tests for TextoCreate model
class TestTextoCreate:
    def test_create_valid_instance(self):
        texto_ocr = generate_unique_text("ocr")
        modelo_ocr = generate_unique_text("model")
        texto_create = TextoCreate(texto_ocr=texto_ocr, modelo_ocr=modelo_ocr)
        assert texto_create.texto_ocr == texto_ocr, "Texto OCR should match the input"
        assert texto_create.modelo_ocr == modelo_ocr, "Modelo OCR should match the input"

    def test_create_invalid_instance_missing_fields(self):
        with pytest.raises(ValidationError):
            TextoCreate()

# Tests for TextoOcrInDatabase model
class TestTextoOcrInDatabase:
    def test_create_valid_instance(self):
        texto_ocr = generate_unique_text("ocr")
        modelo_ocr = generate_unique_text("model")
        pagina_id = 1
        texto_ocr_in_db = TextoOcrInDatabase(texto_ocr=texto_ocr, modelo_ocr=modelo_ocr, pagina_id=pagina_id)
        assert texto_ocr_in_db.texto_ocr == texto_ocr, "Texto OCR should match the input"
        assert texto_ocr_in_db.modelo_ocr == modelo_ocr, "Modelo OCR should match the input"
        assert texto_ocr_in_db.pagina_id == pagina_id, "Pagina ID should match the input"
        assert texto_ocr_in_db.created_at <= datetime.now(), "Created_at should be less than or equal to the current time"
        assert texto_ocr_in_db.updated_at <= datetime.now(), "Updated_at should be less than or equal to the current time"

    def test_create_invalid_instance_missing_fields(self):
        with pytest.raises(ValidationError):
            TextoOcrInDatabase()

# Tests for TextoOcrOut model
class TestTextoOcrOut:
    def test_create_valid_instance(self):
        id = 1
        pagina_id = 1
        texto_ocr = generate_unique_text("ocr")
        modelo_ocr = generate_unique_text("model")
        texto_ocr_out = TextoOcrOut(id=id, pagina_id=pagina_id, texto_ocr=texto_ocr, modelo_ocr=modelo_ocr)
        assert texto_ocr_out.id == id, "ID should match the input"
        assert texto_ocr_out.pagina_id == pagina_id, "Pagina ID should match the input"
        assert texto_ocr_out.texto_ocr == texto_ocr, "Texto OCR should match the input"
        assert texto_ocr_out.modelo_ocr == modelo_ocr, "Modelo OCR should match the input"

    def test_create_invalid_instance_missing_fields(self):
        with pytest.raises(ValidationError):
            TextoOcrOut()
```