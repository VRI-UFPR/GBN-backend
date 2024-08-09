from fastapi import APIRouter, status
from typing import Optional
from src.repository.pagina_repository import PaginaRepository
from src.schemes.pagina import PaginaInDatabase

router = APIRouter()
pagina_repository = PaginaRepository()

@router.get("/", response_model=Optional[PaginaInDatabase], status_code=status.HTTP_200_OK)
async def get_pagina() -> PaginaInDatabase:
    return pagina_repository.get_all()

@router.get("/{id}", response_model=Optional[PaginaInDatabase], status_code=status.HTTP_200_OK)
async def get_pagina(id: int) -> PaginaInDatabase:
    return pagina_repository.get_by_id(id)

@router.post("/", response_model=Optional[PaginaInDatabase], status_code=status.HTTP_201_CREATED)
async def create_pagina(pagina: PaginaInDatabase) -> PaginaInDatabase:
    pagina_repository.create(pagina)
    return pagina