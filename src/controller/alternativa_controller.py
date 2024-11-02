import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.repository.alternativa_repository import AlternativaRepository
from src.schemes.alternativa import AlternativaOut

router = APIRouter()
alternativa_repository = AlternativaRepository()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[Optional[AlternativaOut]], status_code=status.HTTP_200_OK)
async def get_alternativa() -> AlternativaOut:
    return alternativa_repository.get_all()

@router.get("/pergunta/{id}", response_model=Optional[AlternativaOut], status_code=status.HTTP_200_OK)
async def get_alternativa_by_pergunta(id: int) -> AlternativaOut:
    return alternativa_repository.get_by_pergunta_id(id)

@router.get("/{id}", response_model=Optional[AlternativaOut], status_code=status.HTTP_200_OK)
async def get_alternativa(id: int) -> AlternativaOut:
    return alternativa_repository.get_by_id(id)

@router.post("/", response_model=Optional[AlternativaOut], status_code=status.HTTP_201_CREATED)
async def create_alternativa(alternativa: AlternativaOut) -> AlternativaOut:
    alternativa_repository.create(alternativa)
    return alternativa

@router.put("/", response_model=Optional[AlternativaOut], status_code=status.HTTP_200_OK)
async def update_alternativa(alternativa: AlternativaOut) -> AlternativaOut:
    alternativa_repository.update(alternativa)
    return alternativa
