import jwt 
from fastapi import FastAPI, Depends, HTTPException, Request, APIRouter, status

from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.repository.usuario_repository import UsuarioRepository
from src.models.usuario import Usuario
from src.schemes.token import Token, TokenData
import dotenv
import os

# Autenticação com base em JWT

router = APIRouter()
dotenv.load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Localizacao da chave privada
PRIVATE_KEY_LOC = os.getenv("PRIVATE_KEY_LOC") 

# Token expira em 60 minutos
ACCESS_TOKEN_EXPIRE_MINUTES = 60

with open(PRIVATE_KEY_LOC) as file: 
    PRIVATE_KEY = file.read()

# Autentica o usuário
def authenticate_user(email: str):
    usuario_repository = UsuarioRepository()
    user = usuario_repository.get_by_email(email)
    if not user:
        return False
    return user

# Cria o token de accesso
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, PRIVATE_KEY, algorithm="HS256")
    return encoded_jwt

# Rota para autenticar o usuário
@router.post("/token")
async def login(
    form_data: Annotated[TokenData, Depends()], 
    ) -> Token:
    user = authenticate_user(form_data.email)
    if not user:
        usuario_repository = UsuarioRepository()
        usuario_data = Usuario(email=form_data.email, nome=form_data.email)
        usuario_repository.create(usuario_data)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"email": form_data.email}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

# Rota para pegar o usuário atual (logado)
@router.get("/usuario", response_model=Usuario)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Credenciais inválidas",
        headers = {"WWW-Authenticate": "Bearer"}
    )

    expired_exception = HTTPException(
        status_code = 440,
        detail = "Token expirou",
        headers = {"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, PRIVATE_KEY, algorithms=["HS256"])
        email = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)

    except jwt.ExpiredSignatureError:
        raise expired_exception
    
    except jwt.PyJWTError:
        raise credentials_exception

    usuario_repository = UsuarioRepository()
    user = usuario_repository.get_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    
    return user

