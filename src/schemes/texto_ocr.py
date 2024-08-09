import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BaseTextoOcr(BaseModel):
    texto_ocr: str # texto extraido do OCR
    modelo_ocr: str # modelo de OCR utilizado

class TextoCreate(BaseTextoOcr):
    pass

class TextoOcrInDatabase(BaseTextoOcr):
    id: Optional[uuid.UUID] | None  = None
    pagina_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()
