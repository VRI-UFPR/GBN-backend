import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .controller import (
    jornal_router,
    exemplar_router,
    pagina_router,
    texto_ocr_router,
    texto_correcao_manual_router,
    usuario_router,
    pontuacao_router,
    alternativa_router,
    pergunta_router,
)

load_dotenv()

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s ')

app = FastAPI(title="GBN Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prefixing all routers with "/api"
app.include_router(jornal_router, prefix="/api/jornal", tags=["Jornal"])
app.include_router(exemplar_router, prefix="/api/exemplar", tags=["Exemplar"])
app.include_router(pagina_router, prefix="/api/pagina", tags=["Pagina"])
app.include_router(texto_ocr_router, prefix="/api/texto_ocr", tags=["Texto OCR"])
app.include_router(texto_correcao_manual_router, prefix="/api/texto_correcao_manual", tags=["Texto Correcao Manual"])
app.include_router(usuario_router, prefix="/api/usuario", tags=["Usuario"])
app.include_router(pontuacao_router, prefix="/api/pontuacao", tags=["Pontuacao"])
app.include_router(alternativa_router, prefix="/api/alternativa", tags=["Alternativa"])
app.include_router(pergunta_router, prefix="/api/pergunta", tags=["Pergunta"])

