```python
import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError
from your_module import BaseUsuario, UsuarioCreate, UsuarioInDatabase, UsuarioOut

# Helper function to create a user with default or specified attributes
def create_usuario(id=None, nome="Test User", email="test@example.com", created_at=None, updated_at=None):
    usuario_data = {"nome": nome, "email": email}
    if id:
        usuario_data["id"] = id
    if created_at:
        usuario_data["created_at"] = created_at
    if updated_at:
        usuario_data["updated_at"] = updated_at
    return UsuarioInDatabase(**usuario_data)

class TestBaseUsuario:
    def test_base_usuario_creation(self):
        usuario = BaseUsuario(nome="Test User", email="test@example.com")
        assert usuario.nome == "Test User", "Nome should be 'Test User'"
        assert usuario.email == "test@example.com", "Email should be 'test@example.com'"

    def test_base_usuario_invalid_email(self):
        with pytest.raises(ValidationError):
            BaseUsuario(nome="Test User", email="not-an-email")

class TestUsuarioCreate:
    def test_usuario_create_inherits_base(self):
        usuario = UsuarioCreate(nome="Test User", email="test@example.com")
        assert usuario.nome == "Test User", "Nome should be 'Test User'"
        assert usuario.email == "test@example.com", "Email should be 'test@example.com'"

class TestUsuarioInDatabase:
    def test_usuario_in_database_has_id_and_timestamps(self):
        usuario = create_usuario(id=1)
        assert usuario.id == 1, "ID should be 1"
        assert isinstance(usuario.created_at, datetime), "created_at should be a datetime object"
        assert isinstance(usuario.updated_at, datetime), "updated_at should be a datetime object"

    def test_usuario_in_database_timestamps_are_recent(self):
        usuario = create_usuario()
        now = datetime.now()
        assert now - usuario.created_at < timedelta(seconds=1), "created_at should be recent"
        assert now - usuario.updated_at < timedelta(seconds=1), "updated_at should be recent"

class TestUsuarioOut:
    def test_usuario_out_inherits_base_and_has_id(self):
        usuario = UsuarioOut(id=1, nome="Test User", email="test@example.com")
        assert usuario.id == 1, "ID should be 1"
        assert usuario.nome == "Test User", "Nome should be 'Test User'"
        assert usuario.email == "test@example.com", "Email should be 'test@example.com'"
```