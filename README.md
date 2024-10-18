# Getting started

## Passo 1: instalacao PostgreSQL

Siga (esse)[https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart] tutorial que tudo vai dar certo!

## Passo 2: entrar na pasta src

`cd src`

## Passo 3: Criar o arquivo .env

Dentro da pasta src, crie um arquivo chamado `.env`. O arquivo deve conter o seguinte conteudo: 

```
ID_FILE_LOCATION="<PATH_to_utils_id_file>"
DB_STRING="postgresql://<usuario_banco>:<senha_banco>@localhost:5432/<nome_banco>"
DATABASE_URL="postgresql://<usuario_banco>:<senha_banco>@localhost:5432/<nome_banco>"
```

## Passo 4: Instalar pacotes
(Você precisa estar usando o python na versão mínima 3.10)

Dentro da pasta src, rode:
```
pip install -r requirements.txt
```

## Passo 5: Rodar o script de criacao de tabelas e populacao de dados

Ainda dentro da pasta src, rode:
`python3 init_database.py`

## Passo 6: Iniciar o Backend

Instale o fastapi usando o pip correspondente a sua versão do python:
`pip install "fastapi[standard]"`

E então inicie o backend:
`fastapi dev main.py`

