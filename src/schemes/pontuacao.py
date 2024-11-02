import datetime
from pydantic import BaseModel

class BasePontuacao(BaseModel):
    pontuacao: int
    lingua_ocr: str

class PontuacaoCreate(BasePontuacao):
    pass

class PontuacaoInDatabase(BasePontuacao):
    id: int
    usuario_id: int
    pontuacao_id: int
    lingua_ocr: str
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()

class PontuacaoOut(BasePontuacao):
    id: int
    usuario_id: int
    
    pontuacao: int