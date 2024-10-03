import os
import jwt
import pytest
from fastapi import HTTPException
from auth import decode_jwt

# Mock environment variables
os.environ["PRIVATE_KEY"] = "change_me"

def test_decode_jwt_valid_token():
    # Generate a valid token
    token = jwt.encode({"some": "payload"}, os.getenv("PRIVATE_KEY"), algorithm="HS256")
    
    # Call the decode_jwt function
    payload = decode_jwt(token)
    
    assert payload["some"] == "payload"

def test_decode_jwt_invalid_token():
    # Use an invalid token
    token = "invalid.token.here"
    
    with pytest.raises(HTTPException) as excinfo:
        decode_jwt(token)
    
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Token inválido"