from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.texto_correcao_manual import TextoCorrecaoManualOut, TextoCorrecaoManualInDatabase
from src.repository.texto_correcao_manual_repository import TextoCorrecaoManualRepository

router = APIRouter()
texto_correcao_manual_repository = TextoCorrecaoManualRepository()

@router.get("/", response_model=List[Optional[TextoCorrecaoManualOut]], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual() -> TextoCorrecaoManualOut:
    return texto_correcao_manual_repository.get_all()

@router.get("/{id}", response_model=Optional[TextoCorrecaoManualOut], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual(id: int) -> TextoCorrecaoManualOut:
    return texto_correcao_manual_repository.get_by_id(id)

@router.get("/usuario/{usuario_id}", response_model=List[Optional[TextoCorrecaoManualOut]], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual_by_usuario_id(usuario_id: int) -> TextoCorrecaoManualOut:
    return texto_correcao_manual_repository.get_by_usuario_id(usuario_id)

@router.get("/pagina/{pagina_id}", response_model=List[Optional[TextoCorrecaoManualOut]], status_code=status.HTTP_200_OK)
async def get_texto_correcao_manual_by_pagina_id(pagina_id: int) -> TextoCorrecaoManualOut:
    return texto_correcao_manual_repository.get_by_pagina_id(pagina_id)

@router.post("/", response_model=Optional[TextoCorrecaoManualOut], status_code=status.HTTP_201_CREATED)
async def create_texto_correcao_manual(texto_correcao_manual: TextoCorrecaoManualOut) -> TextoCorrecaoManualOut:
    try:
        texto_correcao_manual_repository.create(texto_correcao_manual)
        return texto_correcao_manual
    
    except Exception as e:
        print(e)
    

@router.put("/", response_model=Optional[TextoCorrecaoManualOut], status_code=status.HTTP_200_OK)
async def update_texto_correcao_manual(texto_correcao_manual: TextoCorrecaoManualOut) -> TextoCorrecaoManualOut:
    texto_correcao_manual_repository.update(texto_correcao_manual)
    return texto_correcao_manual