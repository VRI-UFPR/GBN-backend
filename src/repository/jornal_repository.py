from src.repository.base_repository import BaseRepository
from src.models.jornal import Jornal

class JornalRepository:
    def __init__(self):
        self.base_repository = BaseRepository(Jornal)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def create(self, jornal):
        obj = Jornal(**jornal.dict())
        return self.base_repository.create(obj)
    
