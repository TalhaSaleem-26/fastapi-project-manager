from sqlmodel import SQLModel,Field
from app.enums.task import TaskStatus
from pydantic import field_validator  ,model_validator  
from typing import Optional
from app.schemas.user import UserRead
class TaskCreate(SQLModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=4)
    assigned_to: str = Field(min_length=3)
    status: TaskStatus = TaskStatus.PENDING
    internal_note: Optional[str] = None
    user_id:str
    


    @field_validator("title","description","assigned_to","user_id")
    @classmethod
    def validate_value(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")

        return value

    @model_validator(mode="after")
    def validate_task(self):
        if self.status == TaskStatus.COMPLETED and not self.internal_note:
            raise ValueError(
                "Internal note is required when task is completed"
            )

        return self
     
    @model_validator(mode="before")
    @classmethod
    def clean_data(cls, data):

        if isinstance(data, dict):

            for field in ["title", "description", "assigned_to"]:
                value = data.get(field)

                if isinstance(value, str):
                    value = value.strip()

                    if not value:
                        raise ValueError(f"{field} cannot be empty")

                    data[field] = value

        return data


        
        
        
class TaskRead(SQLModel):
        id:str
        title:str=Field(default='')
        description:str=Field(default='')
        assigned_to:str=Field(default='')
        status:TaskStatus
        user_id:str
        user:UserRead
class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = Field(default=None, min_length=4)
    assigned_to: Optional[str] = Field(default=None, min_length=3)
    status: Optional[TaskStatus] = None
    internal_note: Optional[str] = None
        


