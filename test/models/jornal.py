```python
import datetime
from sqlmodel import create_engine, Session, select
from sqlmodel.sql.expression import Select, SelectOfScalar
from unittest.mock import patch
import pytest
from your_module import Jornal  # Assuming the provided code is in a module named your_module

# Patching Select and SelectOfScalar to avoid "TypeError: SelectOfScalar not awaitable" error with pytest-asyncio
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

# Setup for in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=True)


@pytest.fixture(name="session", scope="function")
def session_fixture():
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="function", autouse=True)
def create_test_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


class TestJornalModel:
    def test_create_jornal_should_succeed(self, session):
        jornal_data = {
            "titulo_jornal": "Test Journal",
            "cidade_publicacao": "Test City",
            "estado_publicacao": "Test State",
            "periodo_publicacao": "Test Period",
            "ano_scan": 2023,
        }
        jornal = Jornal(**jornal_data)
        session.add(jornal)
        session.commit()
        session.refresh(jornal)
        assert jornal.id is not None, "Jornal ID should not be None after saving"

    def test_update_jornal_should_succeed(self, session):
        jornal_data = {
            "titulo_jornal": "Initial Title",
            "cidade_publicacao": "Initial City",
            "estado_publicacao": "Initial State",
            "periodo_publicacao": "Initial Period",
            "ano_scan": 2022,
        }
        jornal = Jornal(**jornal_data)
        session.add(jornal)
        session.commit()
        session.refresh(jornal)

        jornal.titulo_jornal = "Updated Title"
        session.commit()
        session.refresh(jornal)
        assert jornal.titulo_jornal == "Updated Title", "Jornal title should be updated"

    def test_delete_jornal_should_succeed(self, session):
        jornal_data = {
            "titulo_jornal": "To Be Deleted",
            "cidade_publicacao": "Some City",
            "estado_publicacao": "Some State",
            "periodo_publicacao": "Some Period",
            "ano_scan": 2021,
        }
        jornal = Jornal(**jornal_data)
        session.add(jornal)
        session.commit()

        session.delete(jornal)
        session.commit()

        result = session.exec(select(Jornal).where(Jornal.id == jornal.id)).first()
        assert result is None, "Jornal should be deleted"

    def test_jornal_created_at_should_be_utcnow(self, session):
        with patch('your_module.datetime') as mock_datetime:
            mock_datetime.datetime.utcnow.return_value = datetime.datetime(2023, 1, 1, 12, 0, 0)
            jornal_data = {
                "titulo_jornal": "Test Journal",
                "cidade_publicacao": "Test City",
                "estado_publicacao": "Test State",
                "periodo_publicacao": "Test Period",
                "ano_scan": 2023,
            }
            jornal = Jornal(**jornal_data)
            session.add(jornal)
            session.commit()
            session.refresh(jornal)
            assert jornal.created_at == datetime.datetime(2023, 1, 1, 12, 0, 0), "created_at should match the mocked datetime"

    def test_jornal_updated_at_should_change_on_update(self, session):
        jornal_data = {
            "titulo_jornal": "Initial Title",
            "cidade_publicacao": "Initial City",
            "estado_publicacao": "Initial State",
            "periodo_publicacao": "Initial Period",
            "ano_scan": 2022,
        }
        jornal = Jornal(**jornal_data)
        session.add(jornal)
        session.commit()
        session.refresh(jornal)

        initial_updated_at = jornal.updated_at
        jornal.titulo_jornal = "Updated Title"
        session.commit()
        session.refresh(jornal)

        assert jornal.updated_at > initial_updated_at, "updated_at should be greater after update"
```