import pytest
from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

async def test_app_startup():
    """App should start and have a title and version"""
    response = await client.get("/")
    assert response.status_code == 404, "Expected 404 status code for root path"
    assert app.title == "GBN Backend", "App title should be 'GBN Backend'"
    assert app.version == "0.1.0", "App version should be '0.1.0'"

# def test_cors_middleware():
#     """CORS middleware should allow all origins"""
#     response = client.options("/jornal")
#     assert response.status_code == 200, "OPTIONS request should be allowed by CORS policy"
#     assert response.headers["access-control-allow-origin"] == "*", "CORS policy should allow all origins"

# def test_jornal_router():
#     """Jornal router should be included and respond to GET request"""
#     response = client.get("/jornal")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_exemplar_router():
#     """Exemplar router should be included and respond to GET request"""
#     response = client.get("/exemplar")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_pagina_router():
#     """Pagina router should be included and respond to GET request"""
#     response = client.get("/pagina")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_texto_ocr_router():
#     """Texto OCR router should be included and respond to GET request"""
#     response = client.get("/texto_ocr")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_texto_correcao_manual_router():
#     """Texto Correcao Manual router should be included and respond to GET request"""
#     response = client.get("/texto_correcao_manual")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_usuario_router():
#     """Usuario router should be included and respond to GET request"""
#     response = client.get("/usuario")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_pontuacao_router():
#     """Pontuacao router should be included and respond to GET request"""
#     response = client.get("/pontuacao")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_alternativa_router():
#     """Alternativa router should be included and respond to GET request"""
#     response = client.get("/alternativa")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"

# def test_pergunta_router():
#     """Pergunta router should be included and respond to GET request"""
#     response = client.get("/pergunta")
#     assert response.status_code == 404, "Expected 404 status code for unimplemented route"