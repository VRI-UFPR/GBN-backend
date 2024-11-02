from src.database.database import get_engine
from sqlmodel import Session, select
from src.repository.base_repository import BaseRepository
from src.models.pergunta import Pergunta
from src.models.alternativa import Alternativa
from src.schemes.pergunta import PerguntaOut, PerguntaComAlternativasOut
from src.schemes.alternativa import AlternativaOut

class PerguntaRepository(BaseRepository):
    def __init__(self):
        self.engine = get_engine()
        self.base_repository = BaseRepository(Pergunta)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_pagina_id(self, id):
        return self.base_repository.get_by_column('pagina_id', id)
    
    def get_by_pagina_id_with_alternativas(self, id):
        with Session(self.engine) as session:
            alternativas = {}
            statement = select(Pergunta).where(Pergunta.pagina_id == id)
            perguntas = session.exec(statement).all()
            # print(f"len: {len(perguntas)}")
            for pergunta in perguntas:
                statement = select(Alternativa).where(Alternativa.pergunta_id == pergunta.id)
                alternativas = session.exec(statement).all()

                print(f"len: {len(alternativas)}")
        
        alternativas_out = [AlternativaOut(
            id=alternativa.id,
            pergunta_id=alternativa.pergunta_id,
            pagina_id=alternativa.pagina_id,
            alternativa=alternativa.alternativa,
            alternativa_correta=alternativa.alternativa_correta
        )
            for alternativa in alternativas]

        pergunta_com_alternativas = PerguntaComAlternativasOut(id=pergunta.id, pagina_id=pergunta.pagina_id, pergunta=pergunta.pergunta, alternativas=alternativas_out)

        return pergunta_com_alternativas
    
    def create(self, pergunta):
        obj = Pergunta(**pergunta.dict())
        return self.base_repository.create(obj)
    
    def update(self, pergunta):
        obj = Pergunta(**pergunta.dict())
        return self.base_repository.update(obj)
    