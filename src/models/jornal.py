import datetime
import uuid
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.exemplar import Exemplar

class Jornal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    titulo_jornal: str = Field(index=True)
    cidade_publicacao: str 
    estado_publicacao: str 
    periodo_publicacao: str
    ano_scan: int
    
    # exemplares: Optional[List["Exemplar"]] = Relationship(back_populates="jornais")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)