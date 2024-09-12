```python
import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError
from uuid import uuid4
from pathlib import Path

# Import the classes from the user's code snippet
from your_module import PerguntaBase, PerguntaCreate, PerguntaInDatabase, PerguntaOut

# Test cases for PerguntaBase
class TestPerguntaBase:
    def test_pergunta_base_creation(self):
        pergunta_text = "Qual é a capital da França?"
        pergunta = PerguntaBase(pergunta=pergunta_text)
        assert pergunta.pergunta == pergunta_text, "PerguntaBase should correctly store the 'pergunta' field"

# Test cases for PerguntaCreate
class TestPerguntaCreate:
    def test_pergunta_create_inherits_base(self):
        pergunta_text = "Qual é o maior planeta do Sistema Solar?"
        pergunta = PerguntaCreate(pergunta=pergunta_text)
        assert pergunta.pergunta == pergunta_text, "PerguntaCreate should inherit 'pergunta' field from PerguntaBase"

# Test cases for PerguntaInDatabase
class TestPerguntaInDatabase:
    def test_pergunta_in_database_creation(self):
        pergunta_text = "Quem pintou a Mona Lisa?"
        pagina_id = 1
        pergunta = PerguntaInDatabase(pergunta=pergunta_text, pagina_id=pagina_id)
        assert pergunta.pergunta == pergunta_text, "PerguntaInDatabase should correctly store the 'pergunta' field"
        assert pergunta.pagina_id == pagina_id, "PerguntaInDatabase should correctly store the 'pagina_id' field"
        assert isinstance(pergunta.created_at, datetime), "PerguntaInDatabase should have a 'created_at' datetime field"
        assert isinstance(pergunta.updated_at, datetime), "PerguntaInDatabase should have an 'updated_at' datetime field"

    def test_pergunta_in_database_default_dates(self):
        pergunta = PerguntaInDatabase(pergunta="Is this a question?", pagina_id=2)
        time_difference = datetime.now() - pergunta.created_at
        assert time_difference < timedelta(seconds=1), "PerguntaInDatabase 'created_at' should default to the current time"
        time_difference = datetime.now() - pergunta.updated_at
        assert time_difference < timedelta(seconds=1), "PerguntaInDatabase 'updated_at' should default to the current time"

# Test cases for PerguntaOut
class TestPerguntaOut:
    def test_pergunta_out_creation(self):
        pergunta_text = "What is the speed of light?"
        pergunta_id = 123
        pagina_id = 3
        pergunta = PerguntaOut(id=pergunta_id, pagina_id=pagina_id, pergunta=pergunta_text)
        assert pergunta.id == pergunta_id, "PerguntaOut should correctly store the 'id' field"
        assert pergunta.pagina_id == pagina_id, "PerguntaOut should correctly store the 'pagina_id' field"
        assert pergunta.pergunta == pergunta_text, "PerguntaOut should correctly store the 'pergunta' field"

# Additional test cases can be added here to cover more scenarios, edge cases, or validation errors.
```