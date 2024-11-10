from src.repository.base_repository import BaseRepository
from src.models.texto_correcao_manual import TextoCorrecaoManual
from src.models.pagina import Pagina

class PaginaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Pagina)
        self.correcao_repository = BaseRepository(TextoCorrecaoManual)
        self.num_paginas = self.base_repository.count()
        self.pagina_atual = 0

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_pagina_unica(self, usuario_id, lingua):
        pagina = self.pagina_atual
        paginas_feitas = []

        self.pagina_atual = (self.pagina_atual + 1) % self.num_paginas
        paginas_usuario = self.base_repository.get_by_column("usuario_id", usuario_id)

        for pag in paginas_usuario:
            paginas_feitas.append(paginas_usuario.pagina_id)

        while pagina in paginas_feitas:
            pagina = (pagina + 1) % self.num_paginas
        
        return self.base_repository.get_by_id_and_column(pagina, "exemplar_id", lingua)
    
    def create(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.create(obj)
    
    def update(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.update(obj)
    