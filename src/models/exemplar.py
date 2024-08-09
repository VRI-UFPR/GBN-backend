import datetime
import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.pagina import Pagina

class Exemplar(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    num_paginas: int
    ano_publicacao: int
    idioma_predominante: str
    metadados: str
    jornal_id: uuid.UUID = Field(default=None, foreign_key="jornal.id")
    paginas: list["Pagina"] = Relationship(back_populates="exemplar")
    created_at: datetime.datetime
    updated_at: datetime.datetime