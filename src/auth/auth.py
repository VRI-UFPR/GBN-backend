import jwt
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
import dotenv
import os

dotenv.load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
PRIVATE_KEY = os.getenv("PRIVATE_KEY") 

async def decode_jwt(request: Request, call_next):
    authorization:  str = request.headers.get("Authorization")

    if authorization:
        if "Bearer " not in authorization:
            raise HTTPException(status_code=401, detail="Token inválido (bearer)")

        token = authorization.split("Bearer ")[1]    
        try:
            payload = jwt.decode(token, PRIVATE_KEY, algorithms=["HS256"])
            request.state.username = payload.get("username")
            request.state.email = payload.get("email")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirou")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido")
    else:
        raise HTTPException(status_code=401, detail="Token não fornecido")

    response = await call_next(request)
    return response

