from src.repository.base_repository import BaseRepository
from src.models.usuario import Usuario 

class UsuarioRepository:
    def __init__(self):
        self.base_repository = BaseRepository(Usuario)
    
    def get_all(self):
        return self.base_repository.get_all()

    def get_by_email(self, email):
        return self.base_repository.get_by_email(email)
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def create(self, usuario):
        obj = Usuario(**usuario.dict())
        return self.base_repository.create(obj)
    
    def update(self, usuario):
        obj = Usuario(**usuario.dict())
        return self.base_repository.update(obj)