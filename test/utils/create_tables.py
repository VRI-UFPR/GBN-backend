```python
import pytest
from unittest.mock import patch, MagicMock

# Assuming the database module and its methods are correctly implemented,
# the following tests aim to ensure the main function behaves as expected
# under different scenarios.

@patch('database.database.create_db_and_tables')
def test_main_ShouldPrintSuccessMessage_WhenDBAndTablesCreatedSuccessfully(mock_create_db_and_tables):
    # Setup: Mock the print function to capture its output
    with patch('builtins.print') as mock_print:
        # Action: Call the main function
        from database.database import main
        main()
        
        # Assert: Check if the success message was printed
        mock_print.assert_called_with("Tabelas criadas")

@patch('database.database.create_db_and_tables')
def test_main_ShouldPrintErrorMessage_WhenExceptionOccurs(mock_create_db_and_tables):
    # Setup: Configure the mock to raise an exception
    mock_create_db_and_tables.side_effect = Exception("Erro ao criar tabelas")
    
    # Mock the print function to capture its output
    with patch('builtins.print') as mock_print:
        # Action: Call the main function
        from database.database import main
        main()
        
        # Assert: Check if the error message was printed
        mock_print.assert_called_with("Erro ao criar tabelas")

# Note: These tests assume that the create_db_and_tables function is correctly
# implemented and will raise an exception if something goes wrong. The tests
# focus on the behavior of the main function when its underlying dependencies
# behave as expected or raise exceptions.
```