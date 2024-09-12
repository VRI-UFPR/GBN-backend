```python
import pytest
from unittest.mock import patch, mock_open
from PIL import Image
import pytesseract
import csv
import os

# Assuming the provided code is saved in a file named `ocr_processor.py`
from ocr_processor import process_ocr  # This is a hypothetical function you would create to encapsulate the provided code for testing

class TestOCRProcessor:
    @pytest.fixture
    def mock_image_open(self, mocker):
        """Fixture to mock PIL.Image.open."""
        mock = mocker.patch('PIL.Image.open', autospec=True)
        mock.return_value.__enter__.return_value = Image.new('RGB', (60, 30), color = 'red')
        return mock

    @pytest.fixture
    def mock_pytesseract(self, mocker):
        """Fixture to mock pytesseract.image_to_string."""
        return mocker.patch('pytesseract.image_to_string', return_value="Mocked OCR Text")

    @pytest.fixture
    def mock_csv_reader(self, mocker):
        """Fixture to mock csv.reader."""
        return mocker.patch('csv.reader', return_value=iter([["id", "some_other_field", "image_path"], ["1", "data", "/path/to/image.jpg"]]))

    @pytest.fixture
    def mock_csv_writer(self, mocker):
        """Fixture to mock csv.writer."""
        m = mock_open()
        mocker.patch('builtins.open', m)
        return mocker.patch('csv.writer')

    def test_process_ocr_reads_image_and_extracts_text(self, mock_image_open, mock_pytesseract, mock_csv_reader, mock_csv_writer):
        process_ocr()
        mock_image_open.assert_called_once_with("/path/to/image.jpg")
        mock_pytesseract.assert_called_once()

    def test_process_ocr_writes_to_csv_correctly(self, mock_image_open, mock_pytesseract, mock_csv_reader, mock_csv_writer):
        process_ocr()
        mock_csv_writer.assert_called()  # Ensure the CSV writer was called to write the output
        handle = mock_csv_writer.call_args[0][0]
        handle.write.assert_called_with('1;tesseract;Mocked OCR Text\n')  # Check if the correct row was written to the CSV

    def test_process_ocr_skips_header_row(self, mocker, mock_csv_reader, mock_csv_writer):
        # Mock csv.reader to return a header row followed by a data row
        mock_csv_reader.return_value = iter([["id", "some_other_field", "image_path"], ["id", "header", "should be skipped"], ["1", "data", "/path/to/image.jpg"]])
        process_ocr()
        # Ensure the CSV writer was called only once for the data row, not the header
        assert mock_csv_writer.call_count == 1, "CSV writer should be called once, skipping the header row"

    def test_process_ocr_handles_missing_image_gracefully(self, mocker, mock_csv_reader, mock_csv_writer):
        mocker.patch('PIL.Image.open', side_effect=FileNotFoundError)
        with pytest.raises(FileNotFoundError):
            process_ocr()
        # Ensure the process does not crash and handles the exception gracefully

    def test_process_ocr_uses_correct_csv_delimiter(self, mock_image_open, mock_pytesseract, mock_csv_reader, mock_csv_writer):
        process_ocr()
        mock_csv_writer.assert_called_with(mocker.ANY, delimiter=';')  # Check if the delimiter ';' is used
```