from src.repository.base_repository import BaseRepository
from src.models.exemplar import Exemplar

class ExemplarRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Exemplar)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def create(self, exemplar):
        obj = Exemplar(**exemplar.dict())
        return self.base_repository.create(obj)
    
    def update(self, exemplar):
        obj = Exemplar(**exemplar.dict())
        return self.base_repository.update(obj)
    