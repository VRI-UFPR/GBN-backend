from src.repository.base_repository import BaseRepository
from src.models.pontuacao import Pontuacao

class PontuacaoRepository:
    def __init__(self):
        self.pontuacao_repository = BaseRepository(Pontuacao)
    
    def get_all(self):
        return self.pontuacao_repository.get_all()
    
    def get_top10(self):
        pontuacao_geral = self.pontuacao_repository.get_all()
        pontuacao_geral.sort(key=lambda x: x.pontuacao, reverse=True)

        return pontuacao_geral[:10]
    
    def get_by_id(self, id):
        return self.pontuacao_repository.get_by_id(id)
    
    def create(self, pontuacao):
        obj = Pontuacao(**pontuacao.dict())
        return self.pontuacao_repository.create(obj)
    
    def update(self, pontuacao):
        obj = Pontuacao(**pontuacao.dict())
        return self.pontuacao_repository.update(obj)