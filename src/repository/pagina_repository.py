import logging

from src.repository.base_repository import BaseRepository
from src.repository.texto_correcao_manual_repository import TextoCorrecaoManualRepository
from src.models.pagina import Pagina

logger = logging.getLogger(__name__)

class PaginaRepository(BaseRepository):
    def __init__(self):
        self.base_repository = BaseRepository(Pagina)
        self.correcao_repository = TextoCorrecaoManualRepository()
        self.num_paginas_portugues = self.base_repository.count_by_column("lingua", "portugues")
        self.num_paginas_alemao = self.base_repository.count_by_column("lingua", "alemao")
        self.pagina_atual_portugues = 0
        self.pagina_atual_alemao = 0

    def get_all(self):
        return self.base_repository.get_all()
    
    def get_by_id(self, id):
        return self.base_repository.get_by_id(id)
    
    def get_pagina_unica(self, usuario_id, lingua):
        paginas_feitas = []
        paginas_lingua = []
        last_page = False

        if lingua == "portugues":
            pagina = self.pagina_atual_portugues
            self.pagina_atual_portugues = (self.pagina_atual_portugues + 1) % self.num_paginas_portugues
        else:
            pagina = self.pagina_atual_alemao
            self.pagina_atual_alemao = (self.pagina_atual_alemao + 1) % self.num_paginas_alemao
    
        paginas_usuario = self.correcao_repository.get_by_usuario_id(usuario_id)
        paginas = self.base_repository.get_by_column_many("lingua", lingua)

        for pag in paginas:
            paginas_lingua.append(pag.id)
        
        for pag in paginas_usuario:
            paginas_feitas.append(paginas_usuario.pagina_id)

        possible_paginas = list(set(paginas_lingua) - set(paginas_feitas))

        if len(possible_paginas) == 1:
            last_page = True

        return self.base_repository.get_by_id_and_column(possible_paginas[pagina], "lingua", lingua), last_page
    
    def create(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.create(obj)
    
    def update(self, pagina):
        obj = Pagina(**pagina.dict())
        return self.base_repository.update(obj)
    