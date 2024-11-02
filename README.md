# Getting started

## Passo 1: instalacao PostgreSQL

Siga (esse)[https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart] tutorial que tudo vai dar certo!

## Passo 2: entrar na pasta src

`cd src`

## Passo 2: Criar o arquivo .env

Dentro da pasta src, crie um arquivo chamado `.env`. O arquivo deve conter o seguinte conteudo: 

```
ID_FILE_LOCATION="<PATH_to_utils_id_file>"
DB_STRING="postgresql://<usuario_banco>:<senha_banco>@localhost:5432/<nome_banco>"
```

## Passo 3: Rodar o script de criacao de tabelas e populacao de dados

`python3 utils/init_database.py`

## Passo 4: Iniciar o Backend

`fastapi dev main.py`

