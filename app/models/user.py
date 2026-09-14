from sqlmodel import SQLModel,Field,Relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.task import Task
    
from uuid import uuid4
def _uuid() ->str:
    return str(uuid4())
    
class User(SQLModel,table=True):
    id:str=Field(primary_key=True,default_factory=_uuid)
    username:str
    email:str
    password:str
    tasks:list["Task"]=Relationship(back_populates="user")