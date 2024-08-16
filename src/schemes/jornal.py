import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel

from src.schemes.exemplar import ExemplarInDatabase

class BaseJornal(BaseModel):
    titulo_jornal: str # nome do Jornal i.e "Der Pionier"
    cidade_publicacao: str # ano de publicação do jornal
    estado_publicacao: str # caminho da pagina do jornal no servidor
    periodo_publicacao: str # periodo de publicação do jornal
    ano_scan: int # ano de publicação do jornal

class JornalCreate(BaseJornal):
    pass

class JornalInDatabase(BaseJornal):
    id: Optional[int] | None  = None
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class JornalOut(BaseJornal):
    id: int
    
    titulo_jornal: str
    cidade_publicacao: str
    estado_publicacao: str
    periodo_publicacao: str
    ano_scan: int