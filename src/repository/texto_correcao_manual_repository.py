from src.repository.base_repository import BaseRepository
from src.models.texto_correcao_manual import TextoCorrecaoManual

class TextoCorrecaoManualRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(TextoCorrecaoManual)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def create(self, texto_correcao_manual):
        obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        return self.base_repository.create(obj)