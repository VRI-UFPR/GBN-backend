import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, SQLModel

class Exemplar(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)

    num_paginas: int
    ano_publicacao: int
    idioma_predominante: str
    metadados: str
    jornal_id: int = Field(default=None, foreign_key="jornal.id")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)