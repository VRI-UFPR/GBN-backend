import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.texto_ocr import TextoOcr
    from models.texto_correcao_manual import TextoCorrecaoManual

class Pagina(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    pagina_index: int
    image_path: str
    exemplar_id: uuid.UUID = Field(default=None, foreign_key="exemplar.id")
    textos_ocr: list["TextoOcr"] = Relationship(back_populates="pagina")
    textos_correcao_manual: list["TextoCorrecaoManual"] = Relationship(back_populates="pagina")
    created_at: datetime.datetime
    updated_at: datetime.datetime