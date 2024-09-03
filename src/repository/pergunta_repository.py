from src.repository.base_repository import BaseRepository
from src.models.pergunta import Pergunta

class PerguntaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Pergunta)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_pagina_id(self, id):
        return self.base_repository.get_by_column('pagina_id', id)
    
    def create(self, pergunta):
        obj = Pergunta(**pergunta.dict())
        return self.base_repository.create(obj)
    
    def update(self, pergunta):
        obj = Pergunta(**pergunta.dict())
        return self.base_repository.update(obj)
    