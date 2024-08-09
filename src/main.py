from fastapi import FastAPI
from .controller import jornal_router, exemplar_router, pagina_router, texto_ocr_router, texto_correcao_manual_router

app = FastAPI(title="GBN Backend", version="0.1.0")

app.include_router(jornal_router, prefix="/jornal", tags=["Jornal"])
app.include_router(exemplar_router, prefix="/exemplar", tags=["Exemplar"])
app.include_router(pagina_router, prefix="/pagina", tags=["Pagina"])
app.include_router(texto_ocr_router, prefix="/texto_ocr", tags=["Texto OCR"])
app.include_router(texto_correcao_manual_router, prefix="/texto_correcao_manual", tags=["Texto Correcao Manual"])


