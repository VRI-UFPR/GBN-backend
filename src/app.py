from database.database import get_engine, create_db_and_tables

def main():
    try:
        create_db_and_tables()
        print("Tabelas criadas")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()