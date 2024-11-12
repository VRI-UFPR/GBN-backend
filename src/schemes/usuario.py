import datetime
from typing import Optional
from pydantic import BaseModel

class BaseUsuario(BaseModel):
    email: str

class UsuarioCreate(BaseUsuario):
    pass

class UsuarioInDatabase(BaseUsuario):
    id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class UsuarioOut(BaseUsuario):
    id: int
    email: str