import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

class TextoCorrecaoManual(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)

    texto_corrigido_manualmente: str # texto extraido do OCR
    
    pagina_id: uuid.UUID = Field(default=None, foreign_key="pagina.id")
    texto_ocr_id: uuid.UUID = Field(default=None, foreign_key="textoocr.id")
    
    created_at: datetime.datetime
    updated_at: datetime.datetime