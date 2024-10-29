from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.texto_correcao_manual import TextoCorrecaoManualOut, TextoCorrecaoManualInDatabase
from src.repository.texto_correcao_manual_repository import TextoCorrecaoManualRepository
from src.repository.texto_ocr_repository import TextoOcrRepository
from src.utils.levenshtein_distance import levenshteinDistance
from src.controller.pontuacao_controller import create_pontuacao
from src.schemes.pontuacao import PontuacaoOut, PontuacaoInDatabase
from fastapi import HTTPException
from Levenshtein import distance

router = APIRouter()
texto_correcao_manual_repository = TextoCorrecaoManualRepository()
texto_ocr_repository = TextoOcrRepository()

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
        # usa 100 como distancia base, por enquanto
        distancia_base = 100
        # pega o texto do texto_correcao_manual
        texto_usuario = texto_correcao_manual.texto_corrigido_manualmente

        # get the ocr_texto from the database
        ocr_base = texto_ocr_repository.get_by_pagina_id(texto_correcao_manual.pagina_id).texto_ocr
        # print("\n\n\ntexto ocr tá aí:\n", ocr_base)
        print("\ndistancia base é :", distancia_base)

        distancia_usuario = distance(ocr_base, texto_usuario)
        print("distaancia do usuario é:", distancia_usuario)

        if distancia_usuario > distancia_base:
            pontuacao = 0
        else:
            pontuacao = round((1 - (distancia_usuario/100)) * 100)
        print("a pontuacao é:", pontuacao)

        pontuacao_data = PontuacaoOut(
            usuario_id=1,
            pontuacao=pontuacao,
            lingua_ocr="Alemão",
            id=1
        )

        await create_pontuacao(pontuacao_data)
        texto_correcao_manual_repository.create(texto_correcao_manual)
        return texto_correcao_manual
    
    except Exception as e:
        print(e)
    

@router.put("/", response_model=Optional[TextoCorrecaoManualOut], status_code=status.HTTP_200_OK)
async def update_texto_correcao_manual(texto_correcao_manual: TextoCorrecaoManualOut) -> TextoCorrecaoManualOut:
    texto_correcao_manual_repository.update(texto_correcao_manual)
    return texto_correcao_manual