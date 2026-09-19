from sqlmodel import Session,select
from app.models.task import Task
from app.schemas.task import TaskUpdate
from fastapi import HTTPException
from app.models.user import User

def create(task: Task,session:Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


def getall(session: Session)-> list[Task]:
    statement=select(Task)
    query=session.exec(statement).all()
    
    return query


def findby_id(taskid:str , session: Session)->Task | None:
    statement=select(Task).where(Task.id==taskid)
    query=session.exec(statement).first()
    
    return query
    
    
def updatetask(taskid: str,task: TaskUpdate,session: Session)->Task:
    statement = select(Task).where(Task.id==taskid)
    data=session.exec(statement).first()
    
    data.title=task.title
    data.description=task.description
    data.assigned_to=task.assigned_to
    data.status=task.status
    
    
    session.add(data)
    session.commit()
    session.refresh(data)
    return data 

    
    


def deleteTask(taskid:str , session : Session)->Task | None:
    statement=select(Task).where(Task.id==taskid)
    query=session.exec(statement).first()
    if (query):
        session.delete(query)
        session.commit()
        return query
    else :
        return None
    
def update_data_patch(
    taskid: str,
    task: TaskUpdate,
    session: Session
) -> Task:

    statement = select(Task).where(Task.id == taskid)
    query = session.exec(statement).first()

    if not query:
        return None

    update_data = task.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(query, field, value)

    session.add(query)
    session.commit()
    session.refresh(query)

    return query

def my_task_repo(current_user:User,session: Session)->list[Task]:
    query=select(Task).where(Task.user_id==current_user.id)
    statement=session.exec(query).all()
    
    return statement
