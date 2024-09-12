# pergunta_controller.py: Pergunta Controller

## Overview

This module defines a FastAPI router for handling operations related to `Pergunta` entities, including retrieving, creating, and updating questions. It interacts with a repository layer to perform database operations.

## Process Flow

```mermaid
graph TD
    Start(Start) --> GetPerguntas["GET /"]
    Start --> GetPerguntaById["GET /{id}"]
    Start --> GetPerguntaByPagina["GET /pagina/{id}"]
    Start --> CreatePergunta["POST /"]
    Start --> UpdatePergunta["PUT /"]

    GetPerguntas --> RepoGetAll["pergunta_repository.get_all()"]
    GetPerguntaById --> RepoGetById["pergunta_repository.get_by_id(id)"]
    GetPerguntaByPagina --> RepoGetByPaginaId["pergunta_repository.get_by_pagina_id(id)"]
    CreatePergunta --> RepoCreate["pergunta_repository.create(pergunta)"]
    UpdatePergunta --> RepoUpdate["pergunta_repository.update(pergunta)"]

    RepoGetAll --> End(End)
    RepoGetById --> End
    RepoGetByPaginaId --> End
    RepoCreate --> End
    RepoUpdate --> End
```

## Insights

- The controller provides endpoints for CRUD operations on `Pergunta` entities.
- It uses dependency injection to interact with the `PerguntaRepository` for database operations.
- The controller handles HTTP status codes, ensuring proper API responses.
- Logging is configured, allowing for monitoring and debugging.
- Type hints are used throughout for clarity and type checking.

## Dependencies

```mermaid
graph LR
    pergunta_controller_py["pergunta_controller.py"] --- |"Uses"| PerguntaRepository["PerguntaRepository"]
    pergunta_controller_py --- |"Returns"| PerguntaOut["PerguntaOut"]
```

- `PerguntaRepository` : The controller uses this for database operations, including fetching, creating, and updating `Pergunta` entities.
- `PerguntaOut` : This schema is used for typing the response models of the API endpoints.