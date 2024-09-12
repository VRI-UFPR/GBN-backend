from database.database import create_db_and_tables
from utils.populate_database import populate_jornal, populate_exemplar, populate_pagina

def main():
    # try:
    #     create_db_and_tables()
    #     print("Tabelas criadas")
    # except Exception as e:
    #     print(e)

    try:
        # populate_jornal()
        populate_exemplar()
        populate_pagina()
        print("Dados populados")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()