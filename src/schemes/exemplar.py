import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BaseExemplar(BaseModel):
    num_paginas: int
    ano_publicacao: int
    idioma_predominante: str
    metadados: str

class ExemplarCreate(BaseExemplar):
    pass

class ExemplarInDatabase(BaseExemplar):
    id: Optional[int] | None  = None
    jornal_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class ExemplarOut(BaseExemplar):
    id: int
    jornal_id: int

    num_paginas: int
    ano_publicacao: int 
    idioma_predominante: str
    metadados: str

