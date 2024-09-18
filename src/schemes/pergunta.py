import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel
from .alternativa import AlternativaOut

class PerguntaBase(BaseModel):
    pergunta: str

class PerguntaCreate(PerguntaBase):
    pass

class PerguntaInDatabase(PerguntaBase):
    id: Optional[int] | None  = None
    pagina_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class PerguntaOut(PerguntaBase):
    id: int
    pagina_id: int
    
    pergunta: str

class PerguntaComAlternativasOut(PerguntaOut):
    alternativas: List[AlternativaOut]