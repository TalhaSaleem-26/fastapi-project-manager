from app.models.task import Task 
from app.models.user import User
from app.schemas.task import TaskCreate,TaskUpdate, TaskRead
from fastapi import HTTPException
from app.repositories.task_repositories import create,getall,findby_id,updatetask,deleteTask,update_data_patch ,my_task_repo
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


def task_by_id(taskid: str, currentuser: User, session: Session) -> Task:
    task = findby_id(taskid, session)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if currentuser.id != task.user_id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to access this task"
        )

    return task



def update_by_id(taskid:str ,task: TaskUpdate , session: Session)->Task:
    data=updatetask(taskid,task,session)
    if(data):
        return data 
    else :
        raise HTTPException(
            status_code=404,
            detail="SomeThing Went Wrong Try Again Later"
        )
    
    
def delete_task(taskid: str, currentuser: User, session: Session) -> Task | None:

    data = deleteTask(taskid, currentuser.id, session)

    if data:
        return data

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


def getting_my_tasks(current_user:User,session: Session)-> list[Task]:
    task=my_task_repo(current_user,session)
    
    if not task :
         return []
        
    return task 

