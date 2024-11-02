from utils.populate_database import populate_all, create_db_and_tables

def main():
    try:
        create_db_and_tables()
        print("Tabelas criadas")
        populate_all()
        print("Dados populados")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()