from datetime import datetime, timedelta
import pytest
from pydantic import ValidationError

# Assuming the provided Python code is defined in a module named `pontuacao_models.py`
from pontuacao_models import BasePontuacao, PontuacaoCreate, PontuacaoInDatabase, PontuacaoOut

class TestBasePontuacao:
    def test_base_pontuacao_creation(self):
        """BasePontuacao should be created with valid pontuacao"""
        pontuacao = BasePontuacao(pontuacao=10)
        assert pontuacao.pontuacao == 10, "Pontuacao should be correctly assigned"

    def test_base_pontuacao_negative_value(self):
        """BasePontuacao should not allow negative pontuacao values"""
        with pytest.raises(ValidationError):
            BasePontuacao(pontuacao=-1)

class TestPontuacaoCreate:
    def test_pontuacao_create_instance(self):
        """PontuacaoCreate should be instantiated correctly"""
        pontuacao_create = PontuacaoCreate(pontuacao=20)
        assert pontuacao_create.pontuacao == 20, "PontuacaoCreate should correctly assign pontuacao"

class TestPontuacaoInDatabase:
    def test_pontuacao_in_database_creation(self):
        """PontuacaoInDatabase should include id, usuario_id, created_at, and updated_at"""
        now = datetime.now()
        pontuacao_in_db = PontuacaoInDatabase(id=1, usuario_id=2, pontuacao=30, created_at=now, updated_at=now)
        assert pontuacao_in_db.id == 1, "ID should be correctly assigned"
        assert pontuacao_in_db.usuario_id == 2, "Usuario ID should be correctly assigned"
        assert pontuacao_in_db.pontuacao == 30, "Pontuacao should be correctly assigned"
        assert pontuacao_in_db.created_at == now, "Created_at should be correctly assigned"
        assert pontuacao_in_db.updated_at == now, "Updated_at should be correctly assigned"

    def test_pontuacao_in_database_default_dates(self):
        """PontuacaoInDatabase should have default values for created_at and updated_at"""
        pontuacao_in_db = PontuacaoInDatabase(id=1, usuario_id=2, pontuacao=40)
        assert pontuacao_in_db.created_at <= datetime.now(), "created_at should have a default value"
        assert pontuacao_in_db.updated_at <= datetime.now(), "updated_at should have a default value"

class TestPontuacaoOut:
    def test_pontuacao_out_creation(self):
        """PontuacaoOut should correctly include id, usuario_id, and pontuacao"""
        pontuacao_out = PontuacaoOut(id=1, usuario_id=2, pontuacao=50)
        assert pontuacao_out.id == 1, "ID should be correctly assigned"
        assert pontuacao_out.usuario_id == 2, "Usuario ID should be correctly assigned"
        assert pontuacao_out.pontuacao == 50, "Pontuacao should be correctly assigned"