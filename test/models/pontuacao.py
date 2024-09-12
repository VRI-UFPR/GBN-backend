```python
import datetime
from unittest.mock import MagicMock
import pytest
from sqlmodel import create_engine, Session, select
from sqlmodel.pool import StaticPool

from your_module import Pontuacao  # Ensure to replace 'your_module' with the actual name of your Python file containing the Pontuacao class.

# Setup for in-memory SQL database for testing
DATABASE_URL = "sqlite://"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

def setup_module(module):
    """Create the database tables for the Pontuacao model before any tests are run."""
    SQLModel.metadata.create_all(engine)

def teardown_module(module):
    """Drop the database tables after all tests have run."""
    SQLModel.metadata.drop_all(engine)

def create_pontuacao(session, usuario_id, pontuacao):
    """Helper function to create a Pontuacao instance for testing."""
    new_pontuacao = Pontuacao(usuario_id=usuario_id, pontuacao=pontuacao)
    session.add(new_pontuacao)
    session.commit()
    session.refresh(new_pontuacao)
    return new_pontuacao

@pytest.fixture(name="session")
def session_fixture():
    """Yields a new database session for a test, ensuring a rollback after the test."""
    with Session(engine) as session:
        yield session
        session.rollback()

class TestPontuacao:
    def test_create_pontuacao_should_succeed(self, session):
        usuario_id = 1
        pontuacao_value = 100
        pontuacao = create_pontuacao(session, usuario_id, pontuacao_value)
        
        assert pontuacao.usuario_id == usuario_id, "The usuario_id should match the one provided"
        assert pontuacao.pontuacao == pontuacao_value, "The pontuacao should match the one provided"
        assert isinstance(pontuacao.created_at, datetime.datetime), "created_at should be a datetime instance"
        assert isinstance(pontuacao.updated_at, datetime.datetime), "updated_at should be a datetime instance"

    def test_update_pontuacao_should_succeed(self, session):
        usuario_id = 1
        pontuacao_value = 100
        new_pontuacao_value = 200
        pontuacao = create_pontuacao(session, usuario_id, pontuacao_value)
        
        pontuacao.pontuacao = new_pontuacao_value
        session.add(pontuacao)
        session.commit()
        session.refresh(pontuacao)
        
        assert pontuacao.pontuacao == new_pontuacao_value, "The pontuacao should be updated to the new value"

    def test_delete_pontuacao_should_succeed(self, session):
        usuario_id = 1
        pontuacao_value = 100
        pontuacao = create_pontuacao(session, usuario_id, pontuacao_value)
        
        session.delete(pontuacao)
        session.commit()
        
        result = session.exec(select(Pontuacao).where(Pontuacao.id == pontuacao.id)).first()
        assert result is None, "The pontuacao should be deleted from the database"

    def test_select_pontuacao_should_return_correct_instance(self, session):
        usuario_id = 1
        pontuacao_value = 100
        pontuacao = create_pontuacao(session, usuario_id, pontuacao_value)
        
        result = session.exec(select(Pontuacao).where(Pontuacao.id == pontuacao.id)).first()
        assert result.id == pontuacao.id, "The selected pontuacao should have the same ID as the created one"
        assert result.usuario_id == usuario_id, "The selected pontuacao should have the correct usuario_id"
        assert result.pontuacao == pontuacao_value, "The selected pontuacao should have the correct pontuacao value"
```