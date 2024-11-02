from src.repository.base_repository import BaseRepository
from src.models.texto_ocr import TextoOcr

class TextoOcrRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(TextoOcr)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_pagina_id(self, pagina_id):
        return self.base_repository.get_by_column("pagina_id", pagina_id)
    
    def create(self, texto_ocr):
        obj = TextoOcr(**texto_ocr.dict())
        return self.base_repository.create(obj)
    
    def update(self, texto_ocr):
        obj = TextoOcr(**texto_ocr.dict())
        return self.base_repository.update(obj)