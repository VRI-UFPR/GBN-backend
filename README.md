# Getting started

## Passo 1: entrar na pasta src

`cd src`

## Passo 2: Criar o arquivo .env

Dentro da pasta src, crie um arquivo chamado `.env`. O arquivo deve conter o seguinte conteudo: 

```
ID_FILE_LOCATION="<PATH_to_utils_id_file>"
DB_STRING="postgresql://<usuario_banco>:<senha_banco>@localhost:5432/<nome_banco>"
PUBLIC_KEY_LOC="<localizacao_da_senha_RSA_publica>"
```

## Passo 3: Rodar o banco e o script de criacao de tabelas e populacao de dados
```
docker compose up -d --build
```
```
docker compose run gbn-backend python init_database.py
```
