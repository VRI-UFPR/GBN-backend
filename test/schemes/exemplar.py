from datetime import datetime, timedelta
import pytest
from pydantic import ValidationError

# Assuming the provided code is in a file named exemplar_models.py
from exemplar_models import ExemplarCreate, ExemplarInDatabase, ExemplarOut

# Helper function to create a common base exemplar for tests
def create_base_exemplar(**kwargs):
    return ExemplarCreate(
        num_paginas=kwargs.get('num_paginas', 100),
        ano_publicacao=kwargs.get('ano_publicacao', 2020),
        idioma_predominante=kwargs.get('idioma_predominante', 'Português'),
        metadados=kwargs.get('metadados', 'alguns metadados')
    )

class TestExemplarModels:
    def test_exemplar_create_should_create_with_valid_data(self):
        exemplar_data = create_base_exemplar()
        assert exemplar_data.num_paginas == 100, "Number of pages should be 100"
        assert exemplar_data.ano_publicacao == 2020, "Publication year should be 2020"
        assert exemplar_data.idioma_predominante == 'Português', "Language should be Portuguese"
        assert exemplar_data.metadados == 'alguns metadados', "Metadata should match"

    def test_exemplar_in_database_should_include_timestamps_and_ids(self):
        exemplar_data = create_base_exemplar()
        exemplar_in_db = ExemplarInDatabase(**exemplar_data.dict(), jornal_id=1)
        assert exemplar_in_db.jornal_id == 1, "Journal ID should be 1"
        assert isinstance(exemplar_in_db.created_at, datetime), "created_at should be a datetime object"
        assert isinstance(exemplar_in_db.updated_at, datetime), "updated_at should be a datetime object"

    def test_exemplar_out_should_output_correct_data(self):
        exemplar_data = create_base_exemplar()
        exemplar_out = ExemplarOut(**exemplar_data.dict(), id=1, jornal_id=1)
        assert exemplar_out.id == 1, "ID should be 1"
        assert exemplar_out.jornal_id == 1, "Journal ID should be 1"
        assert exemplar_out.num_paginas == 100, "Number of pages should be 100"
        assert exemplar_out.ano_publicacao == 2020, "Publication year should be 2020"
        assert exemplar_out.idioma_predominante == 'Português', "Language should be Portuguese"
        assert exemplar_out.metadados == 'alguns metadados', "Metadata should match"

    def test_exemplar_create_with_invalid_data_should_raise_error(self):
        with pytest.raises(ValidationError):
            ExemplarCreate(num_paginas=-1, ano_publicacao=2020, idioma_predominante='Português', metadados='alguns metadados')

    def test_exemplar_in_database_with_future_publication_year_should_raise_error(self):
        future_year = datetime.now().year + 1
        with pytest.raises(ValidationError):
            ExemplarInDatabase(num_paginas=100, ano_publicacao=future_year, idioma_predominante='Português', metadados='alguns metadados', jornal_id=1)

    def test_exemplar_out_with_missing_id_should_raise_error(self):
        exemplar_data = create_base_exemplar()
        with pytest.raises(ValidationError):
            ExemplarOut(**exemplar_data.dict(), jornal_id=1)  # Missing id

    def test_exemplar_in_database_auto_timestamps(self):
        exemplar_data = create_base_exemplar()
        exemplar_in_db = ExemplarInDatabase(**exemplar_data.dict(), jornal_id=1)
        assert exemplar_in_db.created_at <= datetime.now(), "created_at should be less than or equal to the current time"
        assert exemplar_in_db.updated_at <= datetime.now(), "updated_at should be less than or equal to the current time"
        # Simulate an update after 1 second
        exemplar_in_db.updated_at = datetime.now() + timedelta(seconds=1)
        assert exemplar_in_db.updated_at > exemplar_in_db.created_at, "updated_at should be greater than created_at after an update"