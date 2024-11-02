from datetime import datetime, timedelta
import pytest
from pydantic import ValidationError

from your_module import TextoCreate, TextoCorrecaoManualInDatabase, TextoCorrecaoManualOut

# Utility function to create a common base object for tests
def create_base_texto_correcao_manual(texto_corrigido_manualmente="Sample Text"):
    return TextoCreate(texto_corrigido_manualmente=texto_corrigido_manualmente)

# Utility function to create a TextoCorrecaoManualInDatabase object
def create_texto_correcao_manual_in_database(id=None, pagina_id=1, texto_ocr_id=1, texto_corrigido_manualmente="Sample Text"):
    return TextoCorrecaoManualInDatabase(
        id=id,
        pagina_id=pagina_id,
        texto_ocr_id=texto_ocr_id,
        texto_corrigido_manualmente=texto_corrigido_manualmente
    )

# Utility function to create a TextoCorrecaoManualOut object
def create_texto_correcao_manual_out(id=1, pagina_id=1, texto_ocr_id=1, texto_corrigido_manualmente="Sample Text"):
    return TextoCorrecaoManualOut(
        id=id,
        pagina_id=pagina_id,
        texto_ocr_id=texto_ocr_id,
        texto_corrigido_manualmente=texto_corrigido_manualmente
    )

class TestTextoCreate:
    def test_texto_create_valid(self):
        texto = create_base_texto_correcao_manual()
        assert texto.texto_corrigido_manualmente == "Sample Text", "TextoCreate should correctly assign texto_corrigido_manualmente"

    def test_texto_create_empty_text(self):
        with pytest.raises(ValidationError):
            create_base_texto_correcao_manual("")

class TestTextoCorrecaoManualInDatabase:
    def test_texto_correcao_manual_in_database_valid(self):
        texto = create_texto_correcao_manual_in_database()
        assert texto.pagina_id == 1, "Should correctly assign pagina_id"
        assert texto.texto_ocr_id == 1, "Should correctly assign texto_ocr_id"
        assert texto.texto_corrigido_manualmente == "Sample Text", "Should correctly assign texto_corrigido_manualmente"
        assert isinstance(texto.created_at, datetime), "created_at should be a datetime instance"
        assert isinstance(texto.updated_at, datetime), "updated_at should be a datetime instance"

    def test_texto_correcao_manual_in_database_time_auto_set(self):
        texto = create_texto_correcao_manual_in_database()
        now = datetime.now()
        assert now - texto.created_at < timedelta(seconds=1), "created_at should be close to current time"
        assert now - texto.updated_at < timedelta(seconds=1), "updated_at should be close to current time"

class TestTextoCorrecaoManualOut:
    def test_texto_correcao_manual_out_valid(self):
        texto = create_texto_correcao_manual_out()
        assert texto.id == 1, "Should correctly assign id"
        assert texto.pagina_id == 1, "Should correctly assign pagina_id"
        assert texto.texto_ocr_id == 1, "Should correctly assign texto_ocr_id"
        assert texto.texto_corrigido_manualmente == "Sample Text", "Should correctly assign texto_corrigido_manualmente"