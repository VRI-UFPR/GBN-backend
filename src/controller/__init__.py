from .jornal_controller import router as jornal_router
from .exemplar_controller import router as exemplar_router
from .pagina_controller import router as pagina_router
from .texto_ocr_controller import router as texto_ocr_router
from .texto_correcao_manual_controller import router as texto_correcao_manual_router

__all__ = [
    "jornal_router",
    "exemplar_router",
    "pagina_router",
    "texto_ocr_router",
    "texto_correcao_manual_router"
           ]