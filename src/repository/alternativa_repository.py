from src.repository.base_repository import BaseRepository
from src.models.alternativa import Alternativa

class AlternativaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Alternativa)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_pergunta_id(self, id):
        return self.base_repository.get_by_column('pergunta_id', id)
    
    def create(self, alternativa):
        obj = Alternativa(**alternativa.dict())
        return self.base_repository.create(obj)
    
    def update(self, alternativa):
        obj = Alternativa(**alternativa.dict())
        return self.base_repository.update(obj)
