import datetime
import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class TextoOcr(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    
    texto_ocr: str
    modelo_ocr: str

    pagina_id: int = Field(default=None, foreign_key="pagina.id")

    created_at: datetime.datetime
    updated_at: datetime.datetime