```python
import datetime
from unittest.mock import patch
import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool

from your_module import Exemplar  # Assuming the provided code is in your_module.py

# Setup an in-memory SQLite database for testing
@pytest.fixture(name="test_db", scope="module")
def fixture_test_db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(name="session", scope="function")
def fixture_session(test_db):
    connection = test_db.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

class TestExemplar:
    def test_create_exemplar_should_succeed(self, session):
        exemplar = Exemplar(
            num_paginas=100,
            ano_publicacao=2020,
            idioma_predominante="Português",
            metadados="{}",
            jornal_id=1
        )
        session.add(exemplar)
        session.commit()
        assert exemplar.id is not None, "Exemplar ID should not be None after saving"

    def test_update_exemplar_should_reflect_changes(self, session):
        exemplar = Exemplar(
            num_paginas=200,
            ano_publicacao=2019,
            idioma_predominante="Inglês",
            metadados="{}",
            jornal_id=2
        )
        session.add(exemplar)
        session.commit()

        exemplar.num_paginas = 250
        session.commit()

        updated_exemplar = session.get(Exemplar, exemplar.id)
        assert updated_exemplar.num_paginas == 250, "Exemplar num_paginas should be updated to 250"

    def test_delete_exemplar_should_remove_from_db(self, session):
        exemplar = Exemplar(
            num_paginas=300,
            ano_publicacao=2018,
            idioma_predominante="Espanhol",
            metadados="{}",
            jornal_id=3
        )
        session.add(exemplar)
        session.commit()

        session.delete(exemplar)
        session.commit()

        deleted_exemplar = session.get(Exemplar, exemplar.id)
        assert deleted_exemplar is None, "Exemplar should be None after deletion"

    @patch.object(datetime, 'datetime', wraps=datetime.datetime)
    def test_exemplar_created_at_should_be_utcnow(self, mock_datetime, session):
        mock_datetime.utcnow.return_value = datetime.datetime(2021, 1, 1, 12, 0, 0)
        exemplar = Exemplar(
            num_paginas=400,
            ano_publicacao=2017,
            idioma_predominante="Francês",
            metadados="{}",
            jornal_id=4
        )
        session.add(exemplar)
        session.commit()

        assert exemplar.created_at == datetime.datetime(2021, 1, 1, 12, 0, 0), "Exemplar created_at should be set to mocked datetime"

    def test_exemplar_updated_at_should_change_on_update(self, session):
        exemplar = Exemplar(
            num_paginas=500,
            ano_publicacao=2016,
            idioma_predominante="Alemão",
            metadados="{}",
            jornal_id=5
        )
        session.add(exemplar)
        session.commit()

        initial_updated_at = exemplar.updated_at
        exemplar.num_paginas = 550
        session.commit()

        assert exemplar.updated_at > initial_updated_at, "Exemplar updated_at should be greater after update"
```