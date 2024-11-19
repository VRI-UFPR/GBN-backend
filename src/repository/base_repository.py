import datetime
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

    def get_by_email(self, email):
        with Session(self.engine) as session:
            statement = select(self.model).where(self.model.email == email)
            try:
                results = session.exec(statement)
                data = results.one()
            except:
                return None
            
            return data
        
    def get_by_id_and_column(self, id, column, value):
        with Session(self.engine) as session:
            statement = select(self.model).where(self.model.id == id, getattr(self.model, column) == value)
            results = session.exec(statement)
            data = results.one()

            return data
        
    def get_by_column(self, column, value):
        with Session(self.engine) as session:
            statement = select(self.model).where(getattr(self.model, column) == value)
            results = session.exec(statement)
            data = results.one()

            return data
        
    def get_by_column_many(self, column, value):
        with Session(self.engine) as session:
            statement = select(self.model).where(getattr(self.model, column) == value)
            results = session.exec(statement)
            data = results.all()

            return data
    
    def update(self, data):
        with Session(self.engine) as session:
            old_data = session.get(self.model, data.id)
            data_model = data.model_dump(exclude_unset=True)
            old_data.sqlmodel_update(data_model)

            session.add(old_data)
            session.commit()
            session.refresh(old_data)

    def count(self):
        with Session(self.engine) as session:
            statement = select(self.model)
            results = session.exec(statement)
            data = results.all()

            return len(data)
    
    def count_by_column(self, column, value):
        with Session(self.engine) as session:
            statement = select(self.model).where(getattr(self.model, column) == value)
            results = session.exec(statement)
            data = results.all()

            return len(data)
