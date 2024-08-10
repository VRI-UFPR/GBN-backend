import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.pagina import Pagina
    from models.texto_ocr import TextoOcr

class TextoCorrecaoManual(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)

    texto_corrigido_manualmente: str # texto extraido do OCR
    
    pagina_id: uuid.UUID = Field(default=None, foreign_key="pagina.id")
    texto_ocr_id: uuid.UUID = Field(default=None, foreign_key="textoocr.id")

    pagina: "Pagina" = Relationship(back_populates="texto_correcao_manual")
    texto_ocr: "TextoOcr" = Relationship(back_populates="texto_correcao_manual")
    
    created_at: datetime.datetime
    updated_at: datetime.datetime