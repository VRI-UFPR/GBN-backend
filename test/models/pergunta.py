from datetime import datetime, timedelta
import pytest
from sqlmodel import create_engine, Session, select
from sqlmodel.pool import StaticPool
from models import Pergunta  # Assuming the provided code is in a file named models.py

# Setup an in-memory SQLite database for testing
# This avoids affecting a real database and ensures tests run quickly
@pytest.fixture(name="session", scope="session")
def session_fixture():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def create_pergunta(session, pagina_id, pergunta, created_at=None, updated_at=None):
    nova_pergunta = Pergunta(pagina_id=pagina_id, pergunta=pergunta, created_at=created_at, updated_at=updated_at)
    session.add(nova_pergunta)
    session.commit()
    session.refresh(nova_pergunta)
    return nova_pergunta

class TestPerguntaModel:
    def test_create_pergunta_should_succeed(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        pergunta = create_pergunta(session, pagina_id, pergunta_text)
        assert pergunta.id is not None, "Pergunta ID should not be None after creation"
        assert pergunta.pagina_id == pagina_id, "Pergunta pagina_id should match the provided value"
        assert pergunta.pergunta == pergunta_text, "Pergunta text should match the provided value"
        assert isinstance(pergunta.created_at, datetime), "created_at should be a datetime instance"
        assert isinstance(pergunta.updated_at, datetime), "updated_at should be a datetime instance"

    def test_update_pergunta_should_succeed(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        updated_pergunta_text = "What is the capital of Spain?"
        pergunta = create_pergunta(session, pagina_id, pergunta_text)
        
        pergunta.pergunta = updated_pergunta_text
        pergunta.updated_at = datetime.utcnow()
        session.add(pergunta)
        session.commit()

        updated_pergunta = session.get(Pergunta, pergunta.id)
        assert updated_pergunta.pergunta == updated_pergunta_text, "Pergunta text should be updated"
        assert updated_pergunta.updated_at > updated_pergunta.created_at, "updated_at should be greater than created_at after update"

    def test_delete_pergunta_should_succeed(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        pergunta = create_pergunta(session, pagina_id, pergunta_text)
        
        session.delete(pergunta)
        session.commit()

        deleted_pergunta = session.get(Pergunta, pergunta.id)
        assert deleted_pergunta is None, "Pergunta should be None after deletion"

    def test_select_pergunta_should_return_correct_instance(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        create_pergunta(session, pagina_id, pergunta_text)
        
        statement = select(Pergunta).where(Pergunta.pagina_id == pagina_id)
        results = session.exec(statement).first()
        assert results.pergunta == pergunta_text, "Selected Pergunta should have the correct pergunta text"

    def test_pergunta_created_at_should_be_before_updated_at(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        pergunta = create_pergunta(session, pagina_id, pergunta_text)
        
        assert pergunta.created_at <= pergunta.updated_at, "created_at should be less than or equal to updated_at on creation"

    def test_pergunta_updated_at_changes_on_update(self, session):
        pagina_id = 1
        pergunta_text = "What is the capital of France?"
        pergunta = create_pergunta(session, pagina_id, pergunta_text)
        
        original_updated_at = pergunta.updated_at
        pergunta.pergunta = "Updated question"
        pergunta.updated_at = datetime.utcnow()
        session.commit()

        assert pergunta.updated_at > original_updated_at, "updated_at should be greater after an update"