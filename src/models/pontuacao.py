import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Pontuacao(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # usuario_id: int = Field(foreign_key="usuario.id")
    pagina_id: int = Field(foreign_key="pagina.id")
    pontuacao: int
    lingua_ocr: str

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
