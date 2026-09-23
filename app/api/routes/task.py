from fastapi import APIRouter,Depends
from sqlmodel import Session
from app.models.task import Task
from app.schemas.task import TaskCreate,TaskRead,TaskUpdate
from app.db.session import get_session
from app.models.user import User
from app.services.task_service import creating_task,getting_all_tasks,task_by_id,update_by_id,delete_task,patch_dataupdate , getting_user_by_task , getting_my_tasks
from app.core.security import get_current_user
from app.core.security import get_current_user
router=APIRouter(prefix='/task' , tags=['Task'])

@router.post('/create',response_model=TaskRead)
def create_task(task:TaskCreate,session:Session=Depends(get_session))->TaskRead:
    return  creating_task(task,session)

@router.get('/all_tasks',response_model=list[TaskRead])
def all_tasks(session: Session=Depends(get_session))->list[TaskRead]:
    return getting_all_tasks(session)
@router.get("/my-tasks", response_model=list[TaskRead])


def get_my_tasks(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> list[TaskRead]:
    return getting_my_tasks(current_user, session)


@router.get("/{taskid}",response_model=TaskRead)
def get_task_by_id(
    taskid: str,
    currentuser:User=Depends(get_current_user),
    session: Session = Depends(get_session)
) -> TaskRead | None:
    return task_by_id(taskid,currentuser, session)

@router.put("/{taskid}",response_model=TaskRead)
def update_task_by_id(taskid:str ,task: TaskUpdate , session: Session=Depends(get_session))->TaskRead| None:
    return update_by_id(taskid,task,session)

@router.delete("/{taskid}")
def delete_by_id(taskid:str,currentuser:User=Depends(get_current_user),session: Session=Depends(get_session))->Task:
    return delete_task(taskid,currentuser,session)

@router.patch("/{taskid}",response_model=TaskRead)
def patch_updatetask(taskid:str,task:TaskUpdate,session: Session=Depends(get_session))->TaskRead:
    return patch_dataupdate(taskid,task,session)

@router.get("/{taskid}/user",response_model=TaskRead)
def user_by_task(taskid:str,session: Session=Depends(get_session)):
    return getting_user_by_task(taskid,session)

