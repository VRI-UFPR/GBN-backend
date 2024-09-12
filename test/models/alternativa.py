```python
import datetime
import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool
from your_module import Alternativa  # Assuming the provided code is in 'your_module.py'

# Setup for in-memory SQLite database for testing
DATABASE_URL = "sqlite://"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

def setup_module(module):
    SQLModel.metadata.create_all(engine)

def teardown_module(module):
    SQLModel.metadata.drop_all(engine)

def get_test_session():
    with Session(engine) as session:
        yield session

@pytest.fixture
def alternativa_fixture():
    return Alternativa(
        pergunta_id=1,
        pagina_id=1,
        alternativa="Teste Alternativa",
        alternativa_correta=True
    )

class TestAlternativaModel:
    def test_create_alternativa(self, alternativa_fixture):
        with Session(engine) as session:
            session.add(alternativa_fixture)
            session.commit()
            session.refresh(alternativa_fixture)
            assert alternativa_fixture.id is not None, "Should create an Alternativa with an id"

    def test_alternativa_fields(self, alternativa_fixture):
        assert isinstance(alternativa_fixture.pergunta_id, int), "pergunta_id should be an integer"
        assert isinstance(alternativa_fixture.pagina_id, int), "pagina_id should be an integer"
        assert isinstance(alternativa_fixture.alternativa, str), "alternativa should be a string"
        assert isinstance(alternativa_fixture.alternativa_correta, bool), "alternativa_correta should be a boolean"
        assert isinstance(alternativa_fixture.created_at, datetime.datetime), "created_at should be a datetime"
        assert isinstance(alternativa_fixture.updated_at, datetime.datetime), "updated_at should be a datetime"

    def test_update_alternativa(self, alternativa_fixture):
        new_alternativa = "Updated Alternativa"
        with Session(engine) as session:
            alternativa_fixture.alternativa = new_alternativa
            session.add(alternativa_fixture)
            session.commit()
            session.refresh(alternativa_fixture)
            assert alternativa_fixture.alternativa == new_alternativa, "Should update the alternativa field"

    def test_delete_alternativa(self, alternativa_fixture):
        with Session(engine) as session:
            session.add(alternativa_fixture)
            session.commit()
            session.delete(alternativa_fixture)
            session.commit()
            db_alternativa = session.get(Alternativa, alternativa_fixture.id)
            assert db_alternativa is None, "Should delete the Alternativa"

# Additional tests can be added here to cover more scenarios, such as validation errors, relationships with other tables, etc.
```