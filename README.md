# Getting started

## Passo 1: instalacao PostgreSQL

Siga (esse)[https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart] tutorial que tudo vai dar certo!

## Passo 2: Criar o arquivo .env

Dentro da pasta src, crie um arquivo chamado `.env`. O arquivo deve conter o seguinte conteudo: 

```
ID_FILE_LOCATION="<PATH_to_utils_id_file>"
DB_STRING="postgresql://<usuario_banco>:<senha_banco>@localhost:5432/<nome_banco>"
```

## Passo 3: Rodar o script de criacao de tabelas

`python3 app.py`

Ao final do processo voce deverá ver a mensagem "Tabelas Criadas"

## Passo 4: Popular as tabelas

`python3 populate_database.py`

Ao final do processo voce deverá ser capaz de rodar queries nas tableas jornal, exemplar e pagina.

## Passo 5: Iniciar o Backend

`fastapi dev main.py`

