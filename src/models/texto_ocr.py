import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.texto_correcao_manual import TextoCorrecaoManual
    from models.pagina import Pagina

class TextoOcr(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    
    texto_ocr: str
    modelo_ocr: str

    pagina_id: uuid.UUID = Field(default=None, foreign_key="pagina.id")

    pagina: "Pagina" = Relationship(back_populates="texto_ocr")
    textos_correcao_manual: list["TextoCorrecaoManual"] = Relationship(back_populates="texto_ocr")

    created_at: datetime.datetime
    updated_at: datetime.datetime