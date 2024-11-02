```python
import pytest
from unittest.mock import MagicMock
from src.repository.base_repository import BaseRepository
from src.models.usuario import Usuario

# Mocking the Usuario model for testing purposes
@pytest.fixture
def mock_usuario():
    usuario = Usuario(id=1, name="Test User", email="test@example.com")
    return usuario

# Mocking the BaseRepository with a MagicMock, simulating the database operations
@pytest.fixture
def mock_base_repository():
    repository = BaseRepository(model=Usuario)
    repository.base_repository = MagicMock()
    return repository

class TestBaseRepository:
    def test_get_all_should_return_list_of_usuarios(self, mock_base_repository):
        # Arrange
        expected_users = [Usuario(id=1, name="Test User", email="test@example.com")]
        mock_base_repository.base_repository.get_all.return_value = expected_users

        # Act
        result = mock_base_repository.get_all()

        # Assert
        assert result == expected_users, "get_all should return a list of Usuario objects"

    def test_get_by_id_should_return_usuario(self, mock_base_repository, mock_usuario):
        # Arrange
        mock_base_repository.base_repository.get_by_id.return_value = mock_usuario

        # Act
        result = mock_base_repository.get_by_id(1)

        # Assert
        assert result == mock_usuario, "get_by_id should return a single Usuario object"

    def test_create_should_add_usuario(self, mock_base_repository, mock_usuario):
        # Arrange
        mock_base_repository.base_repository.create.return_value = mock_usuario

        # Act
        result = mock_base_repository.create(mock_usuario)

        # Assert
        assert result == mock_usuario, "create should add a new Usuario and return it"

    def test_update_should_modify_usuario(self, mock_base_repository, mock_usuario):
        # Arrange
        updated_usuario = Usuario(id=1, name="Updated User", email="updated@example.com")
        mock_base_repository.base_repository.update.return_value = updated_usuario

        # Act
        result = mock_base_repository.update(updated_usuario)

        # Assert
        assert result == updated_usuario, "update should modify the Usuario and return the updated object"
```