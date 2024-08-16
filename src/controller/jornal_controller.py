import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.jornal import JornalOut
from src.repository.jornal_repository import JornalRepository

logger = logging.getLogger(__name__)
router = APIRouter()
jornal_repository = JornalRepository()

@router.get("/", response_model=List[Optional[JornalOut]], status_code=status.HTTP_200_OK)
async def get_jornals() -> JornalOut:
    logger.info("Getting all jornals")
    journals = jornal_repository.get_all()
    return journals

@router.get("/{id}", response_model=Optional[JornalOut], status_code=status.HTTP_200_OK)
async def get_jornal(id: int) -> JornalOut:
    logger.info(f"Getting jornal with id: {id}")
    journal = jornal_repository.get_by_id(id)
    return journal

@router.post("/", response_model=Optional[JornalOut], status_code=status.HTTP_201_CREATED)
async def create_jornal(jornal: JornalOut) -> JornalOut:
    logger.info("Creating jornal")
    jornal_repository.create(jornal)
    return jornal

@router.put("/", response_model=Optional[JornalOut], status_code=status.HTTP_200_OK)
async def update_jornal(jornal: JornalOut) -> JornalOut:
    logger.info(f"Updating jornal with id {jornal.id}")
    jornal_repository.update(jornal)
    return jornal
