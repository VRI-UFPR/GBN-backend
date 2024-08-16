from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.jornal import JornalOut
from src.repository.jornal_repository import JornalRepository

router = APIRouter()
jornal_repository = JornalRepository()

@router.get("/", response_model=List[Optional[JornalOut]], status_code=status.HTTP_200_OK)
async def get_jornals() -> JornalOut:
    print("get_jornals")
    journals = jornal_repository.get_all()
    return journals

@router.get("/{id}", response_model=Optional[JornalOut], status_code=status.HTTP_200_OK)
async def get_jornal(id: int) -> JornalOut:
    journal = jornal_repository.get_by_id(id)
    return journal

@router.post("/", response_model=Optional[JornalOut], status_code=status.HTTP_201_CREATED)
async def create_jornal(jornal: JornalOut) -> JornalOut:
    jornal_repository.create(jornal)
    return jornal
