```python
import pytest
from datetime import datetime
from pydantic import ValidationError
from src.schemes.exemplar import ExemplarInDatabase
from your_module import JornalCreate, JornalInDatabase, JornalOut

# Sample data for testing
sample_jornal_data = {
    "titulo_jornal": "Der Pionier",
    "cidade_publicacao": "Porto Alegre",
    "estado_publicacao": "RS",
    "periodo_publicacao": "Mensal",
    "ano_scan": 1885
}

def create_jornal_in_database(**kwargs):
    """Utility function to create a JornalInDatabase object with default or overridden attributes."""
    data = sample_jornal_data.copy()
    data.update(kwargs)
    return JornalInDatabase(**data)

@pytest.mark.parametrize("attribute, value", [
    ("titulo_jornal", "O Estado de S. Paulo"),
    ("cidade_publicacao", "São Paulo"),
    ("estado_publicacao", "SP"),
    ("periodo_publicacao", "Diário"),
    ("ano_scan", 1875),
])
def test_jornal_create_with_different_attributes(attribute, value):
    """Test JornalCreate with different attributes to ensure flexibility."""
    jornal_data = sample_jornal_data.copy()
    jornal_data[attribute] = value
    jornal = JornalCreate(**jornal_data)
    assert getattr(jornal, attribute) == value, f"{attribute} should be correctly set in JornalCreate"

def test_jornal_in_database_default_ids():
    """Test JornalInDatabase with default IDs and automatic datetime."""
    jornal = create_jornal_in_database()
    assert jornal.id is None, "Default ID should be None"
    assert isinstance(jornal.created_at, datetime), "created_at should be a datetime instance"
    assert isinstance(jornal.updated_at, datetime), "updated_at should be a datetime instance"

def test_jornal_in_database_with_id():
    """Test JornalInDatabase with a specific ID."""
    jornal = create_jornal_in_database(id=123)
    assert jornal.id == 123, "ID should be correctly set in JornalInDatabase"

def test_jornal_out_structure():
    """Test JornalOut to ensure it contains all required fields."""
    jornal_data = sample_jornal_data.copy()
    jornal_data["id"] = 1
    jornal = JornalOut(**jornal_data)
    for field in ["id", "titulo_jornal", "cidade_publicacao", "estado_publicacao", "periodo_publicacao", "ano_scan"]:
        assert hasattr(jornal, field), f"JornalOut should have a '{field}' attribute"

@pytest.mark.parametrize("invalid_data", [
    {"titulo_jornal": 123},  # Invalid type
    {"cidade_publicacao": None},  # None value
    {"estado_publicacao": ""},  # Empty string
    {"periodo_publicacao": "Anual", "ano_scan": "not a number"},  # ano_scan not a number
])
def test_jornal_create_validation_error(invalid_data):
    """Test JornalCreate with invalid data to ensure it raises ValidationError."""
    with pytest.raises(ValidationError):
        JornalCreate(**invalid_data)

def test_jornal_in_database_datetime_update():
    """Test JornalInDatabase to ensure updated_at can be manually set."""
    initial_datetime = datetime(2020, 1, 1)
    updated_datetime = datetime(2021, 1, 1)
    jornal = create_jornal_in_database(updated_at=initial_datetime)
    assert jornal.updated_at == initial_datetime, "Initial updated_at should be set correctly"
    jornal.updated_at = updated_datetime
    assert jornal.updated_at == updated_datetime, "updated_at should be updatable"
```