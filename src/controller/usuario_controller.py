import logging
from fastapi import APIRouter, status
from typing import Optional, List
from src.schemes.usuario import UsuarioOut, UsuarioCreate
from src.repository.usuario_repository import UsuarioRepository

router = APIRouter()
usuario_repository = UsuarioRepository()

@router.get("/", response_model=List[Optional[UsuarioOut]], status_code=status.HTTP_200_OK)
async def get_usuario() -> UsuarioOut:
    return usuario_repository.get_all()

@router.get("/{id}", response_model=Optional[UsuarioOut], status_code=status.HTTP_200_OK)
async def get_usuario(id: int) -> UsuarioOut:
    return usuario_repository.get_by_id(id)

@router.post("/", response_model=Optional[UsuarioCreate], status_code=status.HTTP_201_CREATED)
async def create_usuario(usuario: UsuarioCreate) -> UsuarioOut:
    try:
        usuario_repository.create(usuario)
        return usuario
    
    except Exception as e:
        print(e)

@router.put("/", response_model=Optional[UsuarioOut], status_code=status.HTTP_200_OK)
async def update_usuario(usuario: UsuarioOut) -> UsuarioOut:
    usuario_repository.update(usuario)
    return usuario