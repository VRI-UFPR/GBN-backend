```python
import datetime
from unittest.mock import MagicMock
import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool

from your_module import TextoOcr  # Assuming the provided code is in a module named your_module

# Setup an in-memory SQLite database for testing
# This avoids affecting a real database and ensures tests run quickly
@pytest.fixture(name="memory_engine")
def fixture_memory_engine():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="session")
def fixture_session(memory_engine):
    with Session(memory_engine) as session:
        yield session

class TestTextoOcrModel:
    def test_create_texto_ocr(self, session):
        # Test creating a TextoOcr record
        texto_ocr_instance = TextoOcr(texto_ocr="Sample OCR text", modelo_ocr="Model 1", pagina_id=1)
        session.add(texto_ocr_instance)
        session.commit()
        session.refresh(texto_ocr_instance)
        assert texto_ocr_instance.id is not None, "TextoOcr record should have an ID after being saved to the database"

    def test_update_texto_ocr(self, session):
        # Test updating a TextoOcr record
        texto_ocr_instance = TextoOcr(texto_ocr="Initial OCR text", modelo_ocr="Model 1", pagina_id=1)
        session.add(texto_ocr_instance)
        session.commit()
        session.refresh(texto_ocr_instance)

        texto_ocr_instance.texto_ocr = "Updated OCR text"
        session.commit()
        session.refresh(texto_ocr_instance)
        assert texto_ocr_instance.texto_ocr == "Updated OCR text", "TextoOcr record should be updated with new text"

    def test_timestamps_on_create(self, session):
        # Test that created_at and updated_at are set upon creation
        texto_ocr_instance = TextoOcr(texto_ocr="Sample OCR text", modelo_ocr="Model 1", pagina_id=1)
        session.add(texto_ocr_instance)
        session.commit()
        session.refresh(texto_ocr_instance)
        assert texto_ocr_instance.created_at is not None, "created_at should be set"
        assert texto_ocr_instance.updated_at is not None, "updated_at should be set"
        assert texto_ocr_instance.created_at == texto_ocr_instance.updated_at, "created_at and updated_at should be equal on creation"

    def test_timestamps_on_update(self, session):
        # Test that updated_at is changed upon update, but created_at remains the same
        texto_ocr_instance = TextoOcr(texto_ocr="Initial OCR text", modelo_ocr="Model 1", pagina_id=1)
        session.add(texto_ocr_instance)
        session.commit()
        session.refresh(texto_ocr_instance)

        initial_created_at = texto_ocr_instance.created_at
        initial_updated_at = texto_ocr_instance.updated_at

        texto_ocr_instance.texto_ocr = "Updated OCR text"
        session.commit()
        session.refresh(texto_ocr_instance)

        assert texto_ocr_instance.created_at == initial_created_at, "created_at should not change on update"
        assert texto_ocr_instance.updated_at != initial_updated_at, "updated_at should change on update"
```