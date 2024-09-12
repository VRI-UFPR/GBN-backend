# texto_ocr_controller.py: Text OCR Controller

## Overview

This module defines a FastAPI controller for operations related to Text OCR (Optical Character Recognition). It provides endpoints for retrieving, creating, and updating OCR text data.

## Process Flow

```mermaid
graph TD
    Start("Start") --> Get_All("/ (GET)")
    Start --> Get_By_ID("/{id} (GET)")
    Start --> Get_By_Pagina_ID("/pagina/{pagina_id} (GET)")
    Start --> Create_Text("/ (POST)")
    Start --> Update_Text("/ (PUT)")

    Get_All --> Repo_Get_All{"texto_ocr_repository.get_all()"}
    Get_By_ID --> Repo_Get_By_ID{"texto_ocr_repository.get_by_id(id)"}
    Get_By_Pagina_ID --> Repo_Get_By_Pagina_ID{"texto_ocr_repository.get_by_pagina_id(pagina_id)"}
    Create_Text --> Repo_Create{"texto_ocr_repository.create(texto_ocr)"}
    Update_Text --> Repo_Update{"texto_ocr_repository.update(texto_ocr)"}

    Repo_Get_All --> End("End")
    Repo_Get_By_ID --> End
    Repo_Get_By_Pagina_ID --> End
    Repo_Create --> End
    Repo_Update --> End
```

## Insights

- The controller provides five main endpoints:
  - A `GET` endpoint at the root path to retrieve all OCR text data.
  - Two `GET` endpoints to retrieve OCR text data by its unique ID or by a page ID.
  - A `POST` endpoint at the root path to create new OCR text data.
  - A `PUT` endpoint at the root path to update existing OCR text data.
- Each endpoint specifies a response model based on `TextoOcrOut` and a corresponding HTTP status code.
- The controller interacts with a repository, `TextoOcrRepository`, to perform CRUD operations on the OCR text data.
- The use of `Optional` in the response model indicates that the endpoints may return `None` if the requested data is not found.

## Dependencies

```mermaid
graph LR
    texto_ocr_controller_py["texto_ocr_controller.py"] --- |"Uses"| texto_ocr_repository_py[("texto_ocr_repository.py")]
    texto_ocr_controller_py --- |"Includes"| texto_ocr_out_py[("texto_ocr.py")]
```

- `texto_ocr_repository.py` : The controller uses functions from `TextoOcrRepository` to interact with the database, including retrieving, creating, and updating OCR text data.
- `texto_ocr.py` : Defines the `TextoOcrOut` schema used as the response model for the controller's endpoints.