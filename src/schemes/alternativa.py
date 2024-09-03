import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class AlternativaBase(BaseModel):
    alternativa: str
    alternativa_correta: bool

class AlternativaCreate(AlternativaBase):
    pass

class AlternativaInDatabase(AlternativaBase):
    id: Optional[int] | None  = None
    pergunta_id: int
    pagina_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class AlternativaOut(AlternativaBase):
    id: int
    pergunta_id: int
    pagina_id: int
    
    alternativa: str
    alternativa_correta: bool
    