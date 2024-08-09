from src.database.database import get_engine
from sqlmodel import Session, select  

class BaseRepository:
    def __init__(self, model):
        self.engine = get_engine()
        self.model = model
    
    def create(self, data):
        with Session(self.engine) as session:
            session.add(data)
            session.commit()
    
    def get_all(self):
        with Session(self.engine) as session:
            statement = select(self.model)
            results = session.exec(statement)
            data = results.all()

            return data
        
    def get_by_id(self, id):
        with Session(self.engine) as session:
            statement = select(self.model).where(self.model.id == id)
            results = session.exec(statement)
            data = results.one()

            return data
    
    def update(self, data):
        with Session(self.engine) as session:
            session.add(data)
            session.commit()
            session.refresh(data)
