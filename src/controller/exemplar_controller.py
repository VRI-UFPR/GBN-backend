from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.exemplar import ExemplarInDatabase
from src.repository.exemplar_repository import ExemplarRepository

router = APIRouter()
exemplar_repository = ExemplarRepository()

@router.get("/", response_model=List[Optional[ExemplarInDatabase]], status_code=status.HTTP_200_OK)
async def get_exemplar() -> ExemplarInDatabase:
    return exemplar_repository.get_all()

@router.get("/{id}", response_model=Optional[ExemplarInDatabase], status_code=status.HTTP_200_OK)
async def get_exemplar(id: int) -> ExemplarInDatabase:
    return exemplar_repository.get_by_id(id)

@router.post("/", response_model=Optional[ExemplarInDatabase], status_code=status.HTTP_201_CREATED)
async def create_exemplar(exemplar: ExemplarInDatabase) -> ExemplarInDatabase:
    exemplar_repository.create(exemplar)
    return exemplar