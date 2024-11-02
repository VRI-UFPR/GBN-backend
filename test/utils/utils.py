```python
import pytest
import os
from unittest.mock import patch
from pathlib import Path

# Assuming the provided code is saved in a file named `pagina_manager.py`
from pagina_manager import get_prox_pagina

class TestGetProxPagina:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, tmp_path):
        # Setup: Create a temporary directory and file for testing
        self.original_id_file_location = os.getenv("ID_FILE_LOCATION")
        test_file = tmp_path / "test_id_file.txt"
        test_file.write_text("0")
        os.environ["ID_FILE_LOCATION"] = str(test_file)
        yield
        # Teardown: Restore the original environment variable
        os.environ["ID_FILE_LOCATION"] = self.original_id_file_location

    def test_get_prox_pagina_initial_state_should_return_1(self):
        assert get_prox_pagina() == "1", "Initial state should return '1'"

    def test_get_prox_pagina_increment_until_18_should_return_18(self):
        for _ in range(17):
            get_prox_pagina()
        assert get_prox_pagina() == "18", "Should return '18' after 18 increments"

    def test_get_prox_pagina_after_18_should_reset_to_0(self):
        for _ in range(18):
            get_prox_pagina()
        assert get_prox_pagina() == "0", "Should reset to '0' after reaching '18'"

    def test_get_prox_pagina_file_content_after_reset(self):
        for _ in range(19):
            get_prox_pagina()
        with open(os.getenv("ID_FILE_LOCATION"), 'r') as file:
            assert file.read() == "0", "File content should be '0' after reset"

    def test_get_prox_pagina_file_content_increment(self):
        get_prox_pagina()
        with open(os.getenv("ID_FILE_LOCATION"), 'r') as file:
            assert file.read() == "1", "File content should increment to '1'"

    @patch.dict(os.environ, {"ID_FILE_LOCATION": "non_existent_file.txt"})
    def test_get_prox_pagina_with_nonexistent_file_should_raise_error(self):
        with pytest.raises(FileNotFoundError):
            get_prox_pagina()
```