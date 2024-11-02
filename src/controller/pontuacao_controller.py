import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.pontuacao import PontuacaoOut, PontuacaoCreate
from src.repository.pontuacao_repository import PontuacaoRepository

router = APIRouter()
pontuacao_repository = PontuacaoRepository()

@router.get("/", response_model=List[Optional[PontuacaoOut]], status_code=status.HTTP_200_OK)
async def get_pontuacao() -> PontuacaoOut:
    return pontuacao_repository.get_all()

@router.get("/top10", response_model=List[Optional[PontuacaoOut]], status_code=status.HTTP_200_OK)
async def get_pontuacao_top10() -> PontuacaoOut:
    return pontuacao_repository.get_top10()


@router.get("/{id}", response_model=Optional[PontuacaoOut], status_code=status.HTTP_200_OK)
async def get_pontuacao(id: int) -> PontuacaoOut:
    return pontuacao_repository.get_by_id(id)

@router.post("/", response_model=Optional[PontuacaoCreate], status_code=status.HTTP_201_CREATED)
async def create_pontuacao(pontuacao: PontuacaoCreate) -> PontuacaoOut:
    try:
        pontuacao_repository.create(pontuacao)
        return pontuacao
    
    except Exception as e:
        print(e)

@router.put("/", response_model=Optional[PontuacaoOut], status_code=status.HTTP_200_OK)
async def update_pontuacao(pontuacao: PontuacaoOut) -> PontuacaoOut:
    pontuacao_repository.update(pontuacao)
    return pontuacao