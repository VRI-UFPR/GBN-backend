import datetime
import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class TextoOcr(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    
    texto_ocr: str
    texto_gabarito: str
    modelo_ocr: str = Field(default="Humano")

    pagina_id: int = Field(default=None, foreign_key="pagina.id")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)