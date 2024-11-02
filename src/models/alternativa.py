import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Alternativa(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)
    pergunta_id: int = Field(default=None, foreign_key="pergunta.id")
    pagina_id: int = Field(default=None, foreign_key="pagina.id")

    alternativa: str
    alternativa_correta: bool

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)