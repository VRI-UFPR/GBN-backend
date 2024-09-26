import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv()
sqlite_url = os.getenv("DATABASE_URL")
engine = create_engine(sqlite_url, echo=True)

def get_engine():
    return engine

