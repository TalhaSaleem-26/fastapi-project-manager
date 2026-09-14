from sqlmodel import SQLModel,Field , Relationship
from typing import Optional , TYPE_CHECKING
from uuid import uuid4

if TYPE_CHECKING:
    from app.models.user import User        


def _uuid()->str:
    return str(uuid4())



class Task(SQLModel,table=True):
    id:str=Field(primary_key=True,default_factory=_uuid)
    title:str=Field(default='')
    description:str=Field(default='')
    assigned_to:str=Field(default='')
    status:str= Field(default="Pending")
    internal_note: str = Field(default="")
    user_id:str=Field(foreign_key="user.id")
    user:"User"=Relationship(back_populates="tasks")