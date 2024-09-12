from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in a file named main.py
import pytest

client = TestClient(app)

# Mock data for testing
mock_texto_correcao_manual_out = TextoCorrecaoManualOut(id=1, content="Test content", corrections="Test corrections")
mock_texto_correcao_create = TextoCorrecaoCreate(content="Test content", corrections="Test corrections")

# Mock repository to avoid actual database interactions
class MockTextoCorrecaoManualRepository:
    def get_all(self):
        return [mock_texto_correcao_manual_out]

    def get_by_id(self, id):
        if id == 1:
            return mock_texto_correcao_manual_out
        return None

    def create(self, texto_correcao_manual):
        return mock_texto_correcao_manual_out

    def update(self, texto_correcao_manual):
        return texto_correcao_manual

# Replace the actual repository with the mock repository
app.dependency_overrides[TextoCorrecaoManualRepository] = MockTextoCorrecaoManualRepository

@pytest.mark.asyncio
async def test_get_texto_correcao_manual():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [mock_texto_correcao_manual_out.dict()]

@pytest.mark.asyncio
async def test_get_texto_correcao_manual_by_id():
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == mock_texto_correcao_manual_out.dict()

@pytest.mark.asyncio
async def test_get_texto_correcao_manual_by_invalid_id():
    response = client.get("/999")
    assert response.status_code == 200
    assert response.json() is None

@pytest.mark.asyncio
async def test_create_texto_correcao_manual():
    response = client.post("/", json=mock_texto_correcao_create.dict())
    assert response.status_code == 201
    assert response.json() == mock_texto_correcao_create.dict()

@pytest.mark.asyncio
async def test_update_texto_correcao_manual():
    updated_content = "Updated content"
    updated_corrections = "Updated corrections"
    updated_texto_correcao_manual = mock_texto_correcao_manual_out.copy(update={"content": updated_content, "corrections": updated_corrections})
    response = client.put("/", json=updated_texto_correcao_manual.dict())
    assert response.status_code == 200
    assert response.json()["content"] == updated_content
    assert response.json()["corrections"] == updated_corrections

# Note: The above tests assume that the FastAPI app is initialized in a file named main.py and that the dependency injection for the repository is correctly set up to be overridden in tests.