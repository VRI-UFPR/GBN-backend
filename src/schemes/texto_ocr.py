import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BaseTextoOcr(BaseModel):
    texto_ocr: str # texto extraido do OCR
    texto_gabarito: str # texto correto
    modelo_ocr: str # modelo de OCR utilizado

class TextoCreate(BaseTextoOcr):
    pass

class TextoOcrInDatabase(BaseTextoOcr):
    id: Optional[int] | None  = None
    pagina_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class TextoOcrOut(BaseTextoOcr):
    id: int
    pagina_id: int
    
    texto_ocr: str
    modelo_ocr: str