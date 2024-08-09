from src.repository.base_repository import BaseRepository
from src.models.pagina import Pagina

class PaginaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Pagina)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def create(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.create(obj)
    