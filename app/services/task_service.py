from app.models.task import Task
from app.schemas.task import TaskCreate,TaskUpdate, TaskRead
from fastapi import HTTPException
from app.repositories.task_repositories import create,getall,findby_id,updatetask,deleteTask,update_data_patch
from app.repositories.user_repositories import find_user_by_id
from sqlmodel import Session
def creating_task(task: TaskCreate, session: Session) -> Task:
    new_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to,
        status=task.status,
        internal_note=task.internal_note,
        user_id=task.user_id
        )
    
    user=find_user_by_id(new_task.user_id,session)
    
    if (user):
     return create(new_task, session)
    else :
        raise HTTPException(
            status_code=404,
            detail="cannot Created - user not Found"
        )

def getting_all_tasks(session: Session)-> list[Task]:
    return getall(session)

def task_by_id(taskid:str,session: Session)->Task | None:
    task= findby_id(taskid,session)
    if(task):
        return task
    else :
        raise HTTPException(
    status_code=404,
    detail="Task not found"
)
        
def update_by_id(taskid:str ,task: TaskUpdate , session: Session)->Task:
    data=updatetask(taskid,task,session)
    if(data):
        return data 
    else :
        raise HTTPException(
            status_code=404,
            detail="SomeThing Went Wrong Try Again Later"
        )
    
    
def delete_task(taskid:str,session: Session)->Task |None:
    data= deleteTask(taskid,session)
    if(data):
        return data
    else :
        raise HTTPException(
            status_code=404,
            detail="Data Not Found"
        )
        
def patch_dataupdate(taskid:str,task:TaskUpdate,session: Session)->Task:
    data=update_data_patch(taskid,task,session)
    if(data):
        return data
    else :
         raise  HTTPException(
             status_code=404,
                         detail="Data Not Found"
         )
         
def getting_user_by_task(taskid:str,session: Session)->TaskRead:
    task=task_by_id(taskid,session)
    
    return task