import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BaseExemplar(BaseModel):
    num_paginas: int # nome do Jornal i.e "Der Pionier"
    ano_publicacao: int # ano de publicação do jornal
    idioma_predominante: str # caminho da pagina do jornal no servidor
    metadados: str # periodo de publicação do jornal

class ExemplarCreate(BaseExemplar):
    pass

class ExemplarInDatabase(BaseExemplar):
    id: Optional[int] | None  = None
    jornal_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()