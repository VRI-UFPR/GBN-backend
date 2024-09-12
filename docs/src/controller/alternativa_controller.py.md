# alternativa_controller.py: Alternativa Controller

## Overview

This module defines an API controller for managing "Alternativa" entities. It provides endpoints for retrieving all alternatives, retrieving alternatives by question ID or by their own ID, and for creating or updating alternatives. The controller uses FastAPI for routing and relies on an `AlternativaRepository` for data access.

## Process Flow

```mermaid
graph TD
    Start("Start") --> Get_All("GET /")
    Start --> Get_By_Pergunta_ID("GET /pergunta/{id}")
    Start --> Get_By_ID("GET /{id}")
    Start --> Create_Alternativa("POST /")
    Start --> Update_Alternativa("PUT /")
    
    Get_All --> Repo_Get_All("AlternativaRepository.get_all()")
    Get_By_Pergunta_ID --> Repo_Get_By_Pergunta_ID("AlternativaRepository.get_by_pergunta_id(id)")
    Get_By_ID --> Repo_Get_By_ID("AlternativaRepository.get_by_id(id)")
    Create_Alternativa --> Repo_Create("AlternativaRepository.create(alternativa)")
    Update_Alternativa --> Repo_Update("AlternativaRepository.update(alternativa)")
    
    Repo_Get_All --> End("End")
    Repo_Get_By_Pergunta_ID --> End
    Repo_Get_By_ID --> End
    Repo_Create --> End
    Repo_Update --> End
```

## Insights

- The controller provides CRUD operations for "Alternativa" entities.
- It uses `AlternativaRepository` for data access, abstracting the database interactions.
- The endpoints return `AlternativaOut` schema objects, ensuring a consistent data format for the API responses.
- Logging is configured, allowing for tracking of operations and errors within the controller.
- The use of `Optional` in response models indicates that some endpoints may return `None`, handling cases where the requested data does not exist.

## Dependencies

```mermaid
graph LR
    alternativa_controller_py["alternativa_controller.py"] --- |"Uses"| AlternativaRepository
    alternativa_controller_py --- |"Returns"| AlternativaOut
```

- `AlternativaRepository` : The controller uses this for all database interactions, including fetching, creating, and updating "Alternativa" entities.
- `AlternativaOut` : This schema defines the structure of the response objects returned by the controller's endpoints.