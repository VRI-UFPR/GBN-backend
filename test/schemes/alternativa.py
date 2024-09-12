import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError

# Import the classes from the provided code
from your_module import AlternativaBase, AlternativaCreate, AlternativaInDatabase, AlternativaOut

# Helper function to generate a valid AlternativaInDatabase object
def create_valid_alternativa_in_database(id=None, pergunta_id=1, pagina_id=1, alternativa="Teste", alternativa_correta=True):
    return AlternativaInDatabase(
        id=id,
        pergunta_id=pergunta_id,
        pagina_id=pagina_id,
        alternativa=alternativa,
        alternativa_correta=alternativa_correta,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

# Tests for AlternativaBase
class TestAlternativaBase:
    def test_alternativa_base_creation(self):
        alternativa_base = AlternativaBase(alternativa="Teste", alternativa_correta=True)
        assert alternativa_base.alternativa == "Teste", "Alternativa should be 'Teste'"
        assert alternativa_base.alternativa_correta is True, "Alternativa correta should be True"

    def test_alternativa_base_invalid_boolean(self):
        with pytest.raises(ValidationError):
            AlternativaBase(alternativa="Teste", alternativa_correta="not a boolean")

# Tests for AlternativaCreate
class TestAlternativaCreate:
    def test_alternativa_create_inherits_alternativa_base(self):
        alternativa_create = AlternativaCreate(alternativa="Teste", alternativa_correta=True)
        assert isinstance(alternativa_create, AlternativaBase), "AlternativaCreate should inherit from AlternativaBase"

# Tests for AlternativaInDatabase
class TestAlternativaInDatabase:
    def test_alternativa_in_database_creation(self):
        alternativa_in_db = create_valid_alternativa_in_database()
        assert alternativa_in_db.pergunta_id == 1, "Pergunta ID should be 1"
        assert alternativa_in_db.pagina_id == 1, "Pagina ID should be 1"
        assert isinstance(alternativa_in_db.created_at, datetime), "created_at should be a datetime object"
        assert isinstance(alternativa_in_db.updated_at, datetime), "updated_at should be a datetime object"

    def test_alternativa_in_database_time_auto_set(self):
        alternativa_in_db = create_valid_alternativa_in_database()
        time_difference = datetime.now() - alternativa_in_db.created_at
        assert time_difference < timedelta(seconds=1), "created_at should be set to the current time"

# Tests for AlternativaOut
class TestAlternativaOut:
    def test_alternativa_out_creation(self):
        alternativa_out = AlternativaOut(id=1, pergunta_id=1, pagina_id=1, alternativa="Teste", alternativa_correta=True)
        assert alternativa_out.id == 1, "ID should be 1"
        assert alternativa_out.pergunta_id == 1, "Pergunta ID should be 1"
        assert alternativa_out.pagina_id == 1, "Pagina ID should be 1"
        assert alternativa_out.alternativa == "Teste", "Alternativa should be 'Teste'"
        assert alternativa_out.alternativa_correta is True, "Alternativa correta should be True"

    def test_alternativa_out_inherits_alternativa_base(self):
        alternativa_out = AlternativaOut(id=1, pergunta_id=1, pagina_id=1, alternativa="Teste", alternativa_correta=True)
        assert isinstance(alternativa_out, AlternativaBase), "AlternativaOut should inherit from AlternativaBase"