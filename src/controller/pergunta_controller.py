import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.repository.pergunta_repository import PerguntaRepository
from src.schemes.pergunta import PerguntaOut, PerguntaComAlternativasOut

router = APIRouter()
pergunta_repository = PerguntaRepository()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[Optional[PerguntaOut]], status_code=status.HTTP_200_OK)
async def get_pergunta() -> PerguntaOut:
    return pergunta_repository.get_all()

@router.get("/pagina/{pagina_id}", response_model=Optional[PerguntaOut], status_code=status.HTTP_200_OK)
async def get_pergunta_by_pagina(pagina_id: int) -> PerguntaOut:
    return pergunta_repository.get_by_pagina_id(pagina_id)

@router.get("/alternativas/pagina/{pagina_id}", response_model=Optional[PerguntaComAlternativasOut], status_code=status.HTTP_200_OK)
async def get_pergunta_alternativas_by_pagina(pagina_id: int) -> PerguntaComAlternativasOut:
    return pergunta_repository.get_by_pagina_id_with_alternativas(pagina_id)

@router.get("/{id}", response_model=Optional[PerguntaOut], status_code=status.HTTP_200_OK)
async def get_pergunta(id: int) -> PerguntaOut:
    return pergunta_repository.get_by_id(id)

@router.post("/", response_model=Optional[PerguntaOut], status_code=status.HTTP_201_CREATED)
async def create_pergunta(pergunta: PerguntaOut) -> PerguntaOut:
    pergunta_repository.create(pergunta)
    return pergunta

@router.put("/", response_model=Optional[PerguntaOut], status_code=status.HTTP_200_OK)
async def update_pergunta(pergunta: PerguntaOut) -> PerguntaOut:
    pergunta_repository.update(pergunta)
    return pergunta

