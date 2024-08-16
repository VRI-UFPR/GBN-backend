import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BasePagina(BaseModel):
    pagina_index: int # pagina do jornal
    image_path: str # caminho da pagina do jornal no servidor

class PaginaCreate(BasePagina):
    pass

class PaginaInDatabase(BasePagina):
    id: Optional[int] | None  = None
    exemplar_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()
    