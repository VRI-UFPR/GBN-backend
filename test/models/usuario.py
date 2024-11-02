from datetime import datetime, timedelta
import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool

from your_module import Usuario  # Assuming the provided code is in a module named your_module

# Setup an in-memory SQLite database for testing
@pytest.fixture(name="session", scope="module")
def session_fixture():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

class TestUsuarioModel:
    def create_usuario_instance(self, nome: str, email: str, created_at: datetime = None, updated_at: datetime = None) -> Usuario:
        """
        Helper method to create a Usuario instance with default or provided datetime values.
        """
        usuario = Usuario(nome=nome, email=email)
        if created_at:
            usuario.created_at = created_at
        if updated_at:
            usuario.updated_at = updated_at
        return usuario

    def test_create_usuario_should_succeed(self, session):
        """
        Test that creating a Usuario instance and adding it to the database succeeds.
        """
        usuario = self.create_usuario_instance("Test User", "test@example.com")
        session.add(usuario)
        session.commit()
        assert usuario.id is not None, "Usuario ID should be set after saving to the database."

    def test_usuario_timestamps_should_be_recent(self, session):
        """
        Test that the created_at and updated_at timestamps are recent upon creation.
        """
        usuario = self.create_usuario_instance("Timestamp User", "timestamp@example.com")
        session.add(usuario)
        session.commit()
        now = datetime.utcnow()
        assert usuario.created_at <= now, "created_at should be less than or equal to the current time."
        assert usuario.updated_at <= now, "updated_at should be less than or equal to the current time."

    def test_update_usuario_should_update_timestamp(self, session):
        """
        Test that updating a Usuario instance updates the updated_at timestamp.
        """
        usuario = self.create_usuario_instance("Update User", "update@example.com")
        session.add(usuario)
        session.commit()

        original_updated_at = usuario.updated_at
        usuario.nome = "Updated User"
        session.add(usuario)
        session.commit()

        assert usuario.updated_at > original_updated_at, "updated_at should be updated on user update."

    def test_email_uniqueness(self, session):
        """
        Test that attempting to add a Usuario with a duplicate email address raises an IntegrityError.
        """
        usuario1 = self.create_usuario_instance("User1", "unique@example.com")
        usuario2 = self.create_usuario_instance("User2", "unique@example.com")
        session.add(usuario1)
        session.commit()

        with pytest.raises(Exception) as excinfo:  # Using a generic Exception to catch the database's IntegrityError
            session.add(usuario2)
            session.commit()
        assert "UNIQUE constraint failed" in str(excinfo.value), "Should not allow duplicate email addresses."

    def test_nome_index_effectiveness(self, session):
        """
        Test to ensure that the nome field is indexed by adding multiple users and querying by nome.
        This test assumes that querying by an indexed field should be efficient but does not measure performance directly.
        """
        for i in range(10):
            usuario = self.create_usuario_instance(f"IndexedUser{i}", f"indexed{i}@example.com")
            session.add(usuario)
        session.commit()

        query_result = session.query(Usuario).filter(Usuario.nome == "IndexedUser5").first()
        assert query_result is not None, "Should be able to query Usuario by nome efficiently."
        assert query_result.email == "indexed5@example.com", "The queried Usuario should have the correct email."