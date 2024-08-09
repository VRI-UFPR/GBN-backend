from fastapi import APIRouter, status
from typing import Optional
from src.schemes.texto_correcao_manual import TextoCorrecaoManualInDatabase
from src.repository.texto_correcao_manual_repository import TextoCorrecaoManualRepository

router = APIRouter()
texto_correcao_manual_repository = TextoCorrecaoManualRepository()

@router.get("/", response_model=Optional[TextoCorrecaoManualInDatabase], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual() -> TextoCorrecaoManualInDatabase:
    return texto_correcao_manual_repository.get_all()

@router.get("/{id}", response_model=Optional[TextoCorrecaoManualInDatabase], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual(id: int) -> TextoCorrecaoManualInDatabase:
    return texto_correcao_manual_repository.get_by_id(id)

@router.post("/", response_model=Optional[TextoCorrecaoManualInDatabase], status_code=status.HTTP_201_CREATED)
async def create_texto_correcao_manual(texto_correcao_manual: TextoCorrecaoManualInDatabase) -> TextoCorrecaoManualInDatabase:
    texto_correcao_manual_repository.create(texto_correcao_manual)
    return texto_correcao_manual