```python
import pytest
from unittest.mock import patch, mock_open
from models.jornal import Jornal
from models.exemplar import Exemplar
from models.pagina import Pagina
from sqlmodel import Session, create_engine
from database.database import get_engine
import os

# Mocking the get_engine function to use an in-memory SQLite database for testing
@pytest.fixture
def mock_engine():
    engine = create_engine("sqlite:///:memory:")
    return engine

# Mocking the CSV file content for each function
jornal_csv_content = """id,titulo_jornal,cidade_publicacao,estado_publicacao,periodo_publicacao,ano_scan
1,Test Jornal,Test City,Test State,Test Period,2023
"""

exemplar_csv_content = """id,jornal_id,num_paginas,ano_publicacao,idioma_predominante,metadados
1,1,100,2023,Portuguese,Test Metadata
"""

pagina_csv_content = """id,pagina_index,image_path,exemplar_id
1,1,/path/to/image,1
"""

# Mocking os.path.exists to always return True
@pytest.fixture(autouse=True)
def mock_os_path_exists():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = True
        yield

# Test for populate_jornal function
@patch("builtins.open", new_callable=mock_open, read_data=jornal_csv_content)
@patch("database.database.get_engine")
def test_populate_jornal_should_add_jornal_to_session(mock_get_engine, mock_file, mock_engine):
    mock_get_engine.return_value = mock_engine
    from populate import populate_jornal

    with Session(mock_engine) as session:
        populate_jornal()
        result = session.query(Jornal).all()
        assert len(result) == 1, "Should add one Jornal to the session"
        assert result[0].titulo_jornal == "Test Jornal", "Jornal title should match"

# Test for populate_exemplar function
@patch("builtins.open", new_callable=mock_open, read_data=exemplar_csv_content)
@patch("database.database.get_engine")
def test_populate_exemplar_should_add_exemplar_to_session(mock_get_engine, mock_file, mock_engine):
    mock_get_engine.return_value = mock_engine
    from populate import populate_exemplar

    with Session(mock_engine) as session:
        populate_exemplar()
        result = session.query(Exemplar).all()
        assert len(result) == 1, "Should add one Exemplar to the session"
        assert result[0].idioma_predominante == "Portuguese", "Exemplar language should match"

# Test for populate_pagina function
@patch("builtins.open", new_callable=mock_open, read_data=pagina_csv_content)
@patch("database.database.get_engine")
def test_populate_pagina_should_add_pagina_to_session(mock_get_engine, mock_file, mock_engine):
    mock_get_engine.return_value = mock_engine
    from populate import populate_pagina

    with Session(mock_engine) as session:
        populate_pagina()
        result = session.query(Pagina).all()
        assert len(result) == 1, "Should add one Pagina to the session"
        assert result[0].image_path == "/path/to/image", "Pagina image path should match"
```