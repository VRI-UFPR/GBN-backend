from .jornal_controller import router as jornal_router
from .exemplar_controller import router as exemplar_router
from .pagina_controller import router as pagina_router
from .texto_ocr_controller import router as texto_ocr_router
from .texto_correcao_manual_controller import router as texto_correcao_manual_router
from .usuario_controller import router as usuario_router
from .pontuacao_controller import router as pontuacao_router
from .alternativa_controller import router as alternativa_router
from .pergunta_controller import router as pergunta_router

__all__ = [
    "jornal_router",
    "exemplar_router",
    "pagina_router",
    "texto_ocr_router",
    "texto_correcao_manual_router",
    "usuario_router",
    "pontuacao_router",
    "alternativa_router",
    "pergunta_router"
           ]