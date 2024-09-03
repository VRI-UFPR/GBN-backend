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

## Passo 3: Rodar o script de criacao de tabelas

`python3 utils/create_tables.py`

Ao final do processo voce deverá ver a mensagem "Tabelas Criadas".

obs.: Pode acontecer do compilador reclamar da importacao das classes conter um `src.`, exclua o mesmo, rode o comando e volte ao estado natural. (EU nao sei pq isso acontece)

## Passo 4: Popular as tabelas

`python3 utils/populate_database.py`

Ao final do processo voce deverá ser capaz de rodar queries nas tableas jornal, exemplar e pagina.

## Passo 5: Iniciar o Backend

`fastapi dev main.py`

