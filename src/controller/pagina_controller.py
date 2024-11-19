import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.repository.pagina_repository import PaginaRepository
from src.schemes.pagina import PaginaOut, PaginaRequest

router = APIRouter()
pagina_repository = PaginaRepository()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[Optional[PaginaOut]], status_code=status.HTTP_200_OK)
async def get_pagina() -> PaginaOut:
    return pagina_repository.get_all()

@router.get("/pagina_unica/{usuario_id}/{lingua}", status_code=status.HTTP_200_OK)
async def get_pagina_unica(usuario_id: int, lingua: str) -> PaginaOut:
    data_out, last_page = pagina_repository.get_pagina_unica(usuario_id, lingua)

    dataout = PaginaOut(
        id=data_out.id,
        exemplar_id=data_out.exemplar_id,
        pagina_index=data_out.pagina_index,
        image_path=data_out.image_path,
        iiif_path=data_out.iiif_path,
        fontes=data_out.fontes,
        lingua=data_out.lingua,
        last_page=last_page
    )

    return dataout

    
    

@router.get("/{id}", response_model=Optional[PaginaOut], status_code=status.HTTP_200_OK)
async def get_pagina(id: int) -> PaginaOut:
    return pagina_repository.get_by_id(id)


@router.post("/", response_model=Optional[PaginaOut], status_code=status.HTTP_201_CREATED)
async def create_pagina(pagina: PaginaOut) -> PaginaOut:
    pagina_repository.create(pagina)
    return pagina

@router.put("/", response_model=Optional[PaginaOut], status_code=status.HTTP_200_OK)
async def update_pagina(pagina: PaginaOut) -> PaginaOut:
    pagina_repository.update(pagina)
    return pagina