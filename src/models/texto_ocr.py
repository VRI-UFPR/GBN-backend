import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.texto_correcao_manual import TextoCorrecaoManual
    from models.pagina import Pagina

class TextoOcr(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    
    texto_ocr: str
    modelo_ocr: str

    pagina_id: int = Field(default=None, foreign_key="pagina.id")

    created_at: datetime.datetime
    updated_at: datetime.datetime