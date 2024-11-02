```python
import pytest
from datetime import datetime, timedelta
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool
from pathlib import Path
from your_module import Pagina  # Ensure to replace 'your_module' with the actual name of your module

# Setup for in-memory SQLite database for testing
DATABASE_URL = "sqlite://"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

def setup_module(module):
    SQLModel.metadata.create_all(engine)

def teardown_module(module):
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="session")
def session_fixture():
    with Session(engine) as session:
        yield session

@pytest.fixture(name="sample_pagina")
def sample_pagina_fixture():
    return Pagina(
        exemplar_id=1,
        pagina_index=10,
        image_path="path/to/image.jpg",
        fontes="Fraktur"
    )

class TestPaginaModel:
    def test_create_pagina_should_succeed(self, session, sample_pagina):
        session.add(sample_pagina)
        session.commit()
        assert sample_pagina.id is not None, "Pagina should have an ID after being added to the database"

    def test_pagina_timestamps_on_create(self, session, sample_pagina):
        session.add(sample_pagina)
        session.commit()
        assert sample_pagina.created_at <= datetime.utcnow(), "Created_at should be set to current time or earlier"
        assert sample_pagina.updated_at <= datetime.utcnow(), "Updated_at should be set to current time or earlier"

    def test_update_pagina_should_update_timestamp(self, session, sample_pagina):
        session.add(sample_pagina)
        session.commit()
        original_updated_at = sample_pagina.updated_at

        sample_pagina.fontes = "Antiqua"
        session.add(sample_pagina)
        session.commit()

        assert sample_pagina.updated_at > original_updated_at, "Updated_at should be updated on record update"

    def test_pagina_with_optional_fields_none(self, session):
        pagina = Pagina(
            exemplar_id=2,
            pagina_index=5,
            fontes="Fraktur"
        )
        session.add(pagina)
        session.commit()
        assert pagina.image_path is None, "Image_path should be able to be None"
        assert pagina.iiif_path is None, "IIIF_path should be able to be None"

    def test_pagina_with_invalid_fontes_should_fail(self, session):
        with pytest.raises(ValueError):
            Pagina(
                exemplar_id=3,
                pagina_index=15,
                fontes="InvalidFont"
            )

    @pytest.mark.parametrize("pagina_index", [-1, 0])
    def test_pagina_with_invalid_pagina_index_should_fail(self, session, pagina_index):
        with pytest.raises(ValueError):
            Pagina(
                exemplar_id=4,
                pagina_index=pagina_index,
                fontes="Fraktur"
            )

    def test_pagina_path_directory_separator(self, session, sample_pagina):
        expected_path = "path" + Path.sep + "to" + Path.sep + "image.jpg"
        assert sample_pagina.image_path.replace("/", Path.sep) == expected_path, "Image_path should use the platform-specific directory separator"
```