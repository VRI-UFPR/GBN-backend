import jwt 
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from src.repository.usuario_repository import UsuarioRepository
from src.models.usuario import Usuario
import dotenv
import os

dotenv.load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
PUBLIC_KEY_LOC = os.getenv("PUBLIC_KEY_LOC") 

with open(PUBLIC_KEY_LOC) as file: 
    PUBLIC_KEY = file.read()

def checkIfUserExists(email: str, username: str):
    usuario_repository = UsuarioRepository()
    user = usuario_repository.get_by_email(email)
    if not user:
        usuario_data = Usuario(email=email, nome=username)
        usuario_repository.create(usuario_data)

async def decode_jwt(request: Request, call_next):
    authorization:  str = request.headers.get("Authorization")

    if authorization:
        if "Bearer " not in authorization:
            raise HTTPException(status_code=401, detail="Token inválido (bearer)")

        token = authorization.split("Bearer ")[1]    
        try:
            payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
            request.state.username = payload.get("username")
            request.state.email = payload.get("email")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirou")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido")
    else:
        raise HTTPException(status_code=401, detail="Token não fornecido")

    # Caso a request seja do tipo POST, checará se o user já existe
    if request.method == "POST" or request.method == "PUT":
        checkIfUserExists(request.state.email, request.state.username)

    response = await call_next(request)
    return response

