import datetime
import uuid
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.exemplar import Exemplar

class Jornal(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    titulo_jornal: str = Field(index=True)
    cidade_publicacao: str 
    estado_publicacao: str 
    periodo_publicacao: str
    ano_scan: int
    exemplares: List["Exemplar"] = Relationship(back_populates="jornal")
    created_at: datetime.datetime
    updated_at: datetime.datetime