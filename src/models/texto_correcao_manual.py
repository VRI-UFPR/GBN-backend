import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.pagina import Pagina
    from models.texto_ocr import TextoOcr

class TextoCorrecaoManual(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    texto_corrigido_manualmente: str # texto extraido do OCR
    
    pagina_id: int = Field(default=None, foreign_key="pagina.id")
    texto_ocr_id: int = Field(default=None, foreign_key="textoocr.id")
    
    created_at: datetime.datetime
    updated_at: datetime.datetime