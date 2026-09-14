from sqlmodel import SQLModel 
from app.models.task import Task
from app.models.user import User
from app.db.engine import engine

def create_tables():
    SQLModel.metadata.create_all(engine)