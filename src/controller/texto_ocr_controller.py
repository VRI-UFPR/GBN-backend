from fastapi import APIRouter, status
from typing import Optional
from src.schemes.texto_ocr import TextoOcrInDatabase
from src.repository.texto_ocr_repository import TextoOcrRepository

router = APIRouter()
texto_ocr_repository = TextoOcrRepository()

@router.get("/", response_model=Optional[TextoOcrInDatabase], status_code=status.HTTP_200_OK)
async def get_texto_ocr() -> TextoOcrInDatabase:
    return texto_ocr_repository.get_all()

@router.get("/{id}", response_model=Optional[TextoOcrInDatabase], status_code=status.HTTP_200_OK)
async def get_texto_ocr(id: int) -> TextoOcrInDatabase:
    return texto_ocr_repository.get_by_id(id)

@router.post("/", response_model=Optional[TextoOcrInDatabase], status_code=status.HTTP_201_CREATED)
async def create_texto_ocr(texto_ocr: TextoOcrInDatabase) -> TextoOcrInDatabase:
    texto_ocr_repository.create(texto_ocr)
    return texto_ocr