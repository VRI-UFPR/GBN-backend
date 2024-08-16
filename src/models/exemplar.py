import datetime
import uuid
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.pagina import Pagina
    from models.jornal import Jornal

class Exemplar(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)

    num_paginas: int
    ano_publicacao: int
    idioma_predominante: str
    metadados: str
    jornal_id: int = Field(default=None, foreign_key="jornal.id")

    # jornais: "Jornal" = Relationship(back_populates="exemplares")
    # paginas: List["Pagina"] = Relationship(back_populates="exemplares")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)