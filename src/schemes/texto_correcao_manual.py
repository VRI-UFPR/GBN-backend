import datetime
from typing import Optional
from pydantic import BaseModel

class BaseTextoCorrecaoManual(BaseModel):
    texto_corrigido_manualmente: str # texto extraido do OCR
    pergunta_resposta_correta: bool

class TextoCreate(BaseTextoCorrecaoManual):
    pass

class TextoCorrecaoManualInDatabase(BaseTextoCorrecaoManual):
    id: Optional[int] | None  = None
    pagina_id: int
    texto_ocr_id: int
    usuario_id: int
    pergunta_id: int
    
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class TextoCorrecaoManualOut(BaseTextoCorrecaoManual):
    id: int
    pagina_id: int
    texto_ocr_id: int
    pergunta_id: int

    usuario_id: int
    texto_corrigido_manualmente: str
    pergunta_resposta_correta: bool
