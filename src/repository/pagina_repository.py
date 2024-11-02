from src.repository.base_repository import BaseRepository
from src.models.pagina import Pagina

class PaginaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Pagina)
        self.num_paginas = self.base_repository.count()
        self.pagina_atual = 0

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_pagina_unica(self):
        pagina = self.pagina_atual
        self.pagina_atual = (self.pagina_atual + 1) % self.num_paginas
        return self.base_repository.get_by_id(pagina)
    
    def create(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.create(obj)
    
    def update(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.update(obj)
    