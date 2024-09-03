import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BasePagina(BaseModel):
    pagina_index: int # pagina do jornal
    image_path: Optional[str] | None = None # caminho da pagina do jornal no servidor
    iiif_path: Optional[str] | None = None # caminho da pagina do jornal no servidor
    fontes: str # fontes da pagina do jornal

class PaginaCreate(BasePagina):
    pass

class PaginaInDatabase(BasePagina):
    id: Optional[int] | None  = None
    exemplar_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class PaginaOut(BasePagina):
    id: int
    exemplar_id: int
    
    pagina_index: int
    image_path: Optional[str] | None = None
    iiif_path: Optional[str] | None = None
    fontes: str
    