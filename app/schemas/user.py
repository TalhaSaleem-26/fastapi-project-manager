from typing import Optional
from sqlmodel import SQLModel,Field
from pydantic import field_validator
from app.models.task import Task
class UserCreate(SQLModel):
    username:str=Field(min_length=3)
    email:str=Field(min_length=5)
    password:str=Field(min_length=4)
    
    @field_validator('username','email','password')
    @classmethod
    def validate_value(cls,value):
        value=value.strip()
        
        if not value:
            raise ValueError("Value Not Found")
        
        return value
    
    
class UserRead(SQLModel):
    id:str
    username:str
    email:str
    
    
    
class UserUpdate(SQLModel):
    username: Optional[str] = Field(default=None, min_length=3)
    email: Optional[str] = Field(default=None, min_length=5)
    password: Optional[str] = Field(default=None, min_length=4)
    
    @field_validator("username", "email", "password")
    @classmethod
    def validate_value(cls, value):
        
         if value is None:
             return value
         
         value = value.strip()

         if not value:
           raise ValueError("Kindly Enter The Data")
        
         return value
     

class UserWithTasks(SQLModel):
    id:str
    username:str
    email:str
    tasks:list["Task"]
    
    
class UserLogin(SQLModel):
    email: str
    password: str
    
    
class Token(SQLModel):
    access_token: str
    token_type: str