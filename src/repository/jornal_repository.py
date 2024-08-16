import logging
from src.repository.base_repository import BaseRepository
from src.models.jornal import Jornal

logger = logging.getLogger(__name__)

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
    
    def update(self, jornal):
        obj = Jornal(**jornal.dict())
        logger.info(f"Updating jornal: {obj}")
        return self.base_repository.update(obj)