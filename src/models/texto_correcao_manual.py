import datetime
import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class TextoCorrecaoManual(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    texto_corrigido_manualmente: str
    pergunta_resposta_correta: bool
    
    pagina_id: int = Field(default=None, foreign_key="pagina.id")
    texto_ocr_id: int = Field(default=None, foreign_key="textoocr.id")
    usuario_id: int = Field(default=None, foreign_key="usuario.id")
    pergunta_id: int = Field(default=None, foreign_key="pergunta.id")
    
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)