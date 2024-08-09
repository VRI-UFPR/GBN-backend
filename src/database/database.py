from sqlmodel import SQLModel, create_engine

sqlite_url = f"postgresql://usergbn:GBN123@localhost:5432/gdbbackend"

def get_engine():
    return create_engine(sqlite_url, echo=True)

def create_db_and_tables(engine) -> None:
    SQLModel.metadata.create_all(engine)