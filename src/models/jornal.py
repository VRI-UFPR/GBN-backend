import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, SQLModel

class Jornal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    titulo_jornal: str = Field(index=True)
    cidade_publicacao: str 
    estado_publicacao: str 
    periodo_publicacao: str
    ano_scan: int

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)