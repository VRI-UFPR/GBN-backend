import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Pagina(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)
    exemplar_id: int = Field(default=None, foreign_key="exemplar.id")

    pagina_index: int
    image_path: Optional[str] | None = None
    iiif_path: Optional[str] | None = None
    fontes: str = Field(default="Fraktur")
    lingua: str = Field(default="alemao")


    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)