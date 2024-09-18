from database.database import create_db_and_tables
from utils.populate_database import populate_all
def main():
    # try:
    #     create_db_and_tables()
    #     print("Tabelas criadas")
    # except Exception as e:
    #     print(e)

    try:
        populate_all()
        print("Dados populados")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()