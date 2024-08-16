from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.texto_ocr import TextoOcrOut
from src.repository.texto_ocr_repository import TextoOcrRepository

router = APIRouter()
texto_ocr_repository = TextoOcrRepository()

@router.get("/", response_model=List[Optional[TextoOcrOut]], status_code=status.HTTP_200_OK)
async def get_texto_ocr() -> TextoOcrOut:
    return texto_ocr_repository.get_all()

@router.get("/{id}", response_model=Optional[TextoOcrOut], status_code=status.HTTP_200_OK)
async def get_texto_ocr(id: int) -> TextoOcrOut:
    return texto_ocr_repository.get_by_id(id)

@router.post("/", response_model=Optional[TextoOcrOut], status_code=status.HTTP_201_CREATED)
async def create_texto_ocr(texto_ocr: TextoOcrOut) -> TextoOcrOut:
    texto_ocr_repository.create(texto_ocr)
    return texto_ocr