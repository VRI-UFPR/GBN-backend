import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Pergunta(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)
    pagina_id: int = Field(default=None, foreign_key="pagina.id")
    
    pergunta: str
    
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)