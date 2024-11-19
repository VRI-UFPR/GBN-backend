from src.repository.base_repository import BaseRepository
from src.models.texto_correcao_manual import TextoCorrecaoManual
from src.models.pontuacao import Pontuacao
from sqlalchemy.orm.exc import NoResultFound

from src.schemes.pontuacao import PontuacaoInDatabase
from src.repository.texto_ocr_repository import TextoOcrRepository
from Levenshtein import distance

class TextoCorrecaoManualRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(TextoCorrecaoManual)
        self.pontuacao_repository = BaseRepository(Pontuacao)

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_by_usuario_id(self, usuario_id):
        try:
            return self.base_repository.get_by_column("usuario_id", usuario_id)
        except NoResultFound:
            return []
    
    def get_by_pagina_id(self, pagina_id):
        return self.base_repository.get_by_column("pagina_id", pagina_id)
    
    def create(self, texto_correcao_manual):
        obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        return self.base_repository.create(obj)
    
    def salvar_resposta(self, texto_correcao_manual):
        texto_ocr_repository = TextoOcrRepository()

        texto_usuario = texto_correcao_manual.texto_corrigido_manualmente
        ocr_base = texto_ocr_repository.get_by_pagina_id(texto_correcao_manual.pagina_id).texto_ocr

        distancia_usuario = distance(ocr_base, texto_usuario)

        print("a pontuacao é:", distancia_usuario)

        pontuacao_data = PontuacaoInDatabase(
            pagina_id=texto_correcao_manual.pagina_id,
            pontuacao=distancia_usuario,
            lingua_ocr="Alemão",
        )

        texto_correcao_manual_obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        pontuacao_obj = Pontuacao(**pontuacao_data.dict())
        
        self.pontuacao_repository.create(pontuacao_obj)
        self.base_repository.create(texto_correcao_manual_obj)
    
    def update(self, texto_correcao_manual):
        obj = TextoCorrecaoManual(**texto_correcao_manual.dict())
        return self.base_repository.update(obj)