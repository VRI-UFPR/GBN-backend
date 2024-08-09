import datetime
import uuid
from typing import Optional
from pydantic import BaseModel

class BaseTextoCorrecaoManual(BaseModel):
    texto_corrigido_manualmente: str # texto extraido do OCR

class TextoCreate(BaseTextoCorrecaoManual):
    pass

class TextoCorrecaoManualInDatabase(BaseTextoCorrecaoManual):
    id: Optional[uuid.UUID] | None  = None
    pagina_id: int
    texto_tesseract_id: int
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()
