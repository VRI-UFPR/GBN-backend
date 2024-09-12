from src.repository.base_repository import BaseRepository
from src.models.texto_correcao_manual import TextoCorrecaoManual

class TextoCorrecaoManualRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(TextoCorrecaoManual)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_usuario_id(self, usuario_id):
        return self.base_repository.get_by_column("usuario_id", usuario_id)
    
    def get_by_pagina_id(self, pagina_id):
        return self.base_repository.get_by_column("pagina_id", pagina_id)
    
    def create(self, texto_correcao_manual):
        obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        return self.base_repository.create(obj)
    
    def update(self, texto_correcao_manual):
        obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        return self.base_repository.update(obj)