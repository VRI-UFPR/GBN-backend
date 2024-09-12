from models.jornal import Jornal
from models.exemplar import Exemplar
from models.pagina import Pagina
from sqlmodel import Session
from database.database import get_engine
import csv

def populate_jornal():
    engine = get_engine()
    with Session(engine) as session:
        with open('/home/pedro/src/GBN-backend/src/data/jornal.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # print(row)                
                jornal = Jornal(id=row[0], titulo_jornal=row[1], cidade_publicacao=row[2], estado_publicacao=row[3], periodo_publicacao=row[4],  ano_scan=row[5])

                session.add(jornal)
                session.commit()

def populate_exemplar():
    engine = get_engine()
    with Session(engine) as session:
        with open('/home/pedro/src/GBN-backend/src/data/exemplar.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # print(row)                
                exemplar = Exemplar(id=row[0], jornal_id=row[1], num_paginas=row[2], ano_publicacao=row[3], idioma_predominante=row[4],  metadados=row[5])

                session.add(exemplar)
                session.commit()

def populate_pagina():
    engine = get_engine()
    with Session(engine) as session:
        with open('/home/pedro/src/GBN-backend/src/data/pagina.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # print(row)                
                pagina = Pagina(id=row[0], pagina_index=row[1], image_path=row[2], exemplar_id=row[3])

                session.add(pagina)
                session.commit()

populate_jornal()
populate_exemplar()
populate_pagina()