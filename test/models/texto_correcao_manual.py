:::CODE_CONVENTIONS > BEGIN
- Use descriptive variable names that convey the purpose of the variable.
- Follow PEP 8 style guide for Python code.
- Use `assert` statements to check for expected outcomes in tests.
- Use `pytest` fixtures for setup and teardown of test data.
- Use `parametrize` for testing different inputs and expected outputs.
- Use `mock` for simulating external dependencies or behaviors.
- Use `capsys` for capturing print outputs if needed.
- Use `tmp_path` for creating temporary files or directories.
- Document the purpose of the test and any specific setup or assertions as comments.
- Use `datetime` module for handling dates and times.
- Use `uuid` for generating unique identifiers.
- Use `SQLModel` for defining database models.
- Use `Field` for defining model fields, including primary keys, foreign keys, and default values.
:::CODE_CONVENTIONS > END

```python
import pytest
from sqlmodel import create_engine, Session, select
from sqlmodel.pool import StaticPool
from datetime import datetime, timedelta
from models import TextoCorrecaoManual  # Assuming the provided code is saved in models.py

# Setup an in-memory SQLite database for testing
@pytest.fixture(name="test_db")
def fixture_test_db():
    # Create an in-memory SQLite database
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(name="session")
def session_fixture(test_db):
    with Session(test_db) as session:
        yield session

def create_texto_correcao_manual(session, texto_corrigido_manualmente="Teste", pagina_id=1, texto_ocr_id=1):
    texto_correcao_manual = TextoCorrecaoManual(
        texto_corrigido_manualmente=texto_corrigido_manualmente,
        pagina_id=pagina_id,
        texto_ocr_id=texto_ocr_id
    )
    session.add(texto_correcao_manual)
    session.commit()
    session.refresh(texto_correcao_manual)
    return texto_correcao_manual

def test_create_texto_correcao_manual(session):
    texto_correcao_manual = create_texto_correcao_manual(session, "Texto de teste", 2, 3)
    assert texto_correcao_manual.texto_corrigido_manualmente == "Texto de teste", "The texto_corrigido_manualmente should be 'Texto de teste'"
    assert texto_correcao_manual.pagina_id == 2, "The pagina_id should be 2"
    assert texto_correcao_manual.texto_ocr_id == 3, "The texto_ocr_id should be 3"

def test_texto_correcao_manual_timestamps(session):
    before_creation = datetime.utcnow()
    texto_correcao_manual = create_texto_correcao_manual(session)
    after_creation = datetime.utcnow()

    assert before_creation <= texto_correcao_manual.created_at <= after_creation, "created_at should be within the test execution time"
    assert before_creation <= texto_correcao_manual.updated_at <= after_creation, "updated_at should be within the test execution time"

def test_update_texto_correcao_manual(session):
    texto_correcao_manual = create_texto_correcao_manual(session)
    session.refresh(texto_correcao_manual)
    updated_text = "Updated text"
    texto_correcao_manual.texto_corrigido_manualmente = updated_text
    session.commit()

    assert texto_correcao_manual.texto_corrigido_manualmente == updated_text, "The texto_corrigido_manualmente should be updated"

def test_select_texto_correcao_manual(session):
    create_texto_correcao_manual(session, "Texto para seleção", 4, 5)
    statement = select(TextoCorrecaoManual).where(TextoCorrecaoManual.pagina_id == 4)
    results = session.exec(statement).first()

    assert results.texto_corrigido_manualmente == "Texto para seleção", "Should be able to retrieve the inserted record by pagina_id"
```