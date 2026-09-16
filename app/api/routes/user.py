from sqlmodel import Session 
from fastapi import APIRouter ,Depends
from app.models.user import User
from app.schemas.user import UserRead,UserCreate,UserUpdate,UserWithTasks ,UserLogin
from app.db.session import get_session
from app.services.user_service import create_user_service , get_all_user_service,getuserby_id,updateuserby_id,deleteuserby_id , getting_user_tasks , login_user_service
userrouter=APIRouter(
    prefix='/user',
    tags=["User"]
)
@userrouter.post('/create',response_model=UserRead)
def create_user(user:UserCreate,session:Session=Depends(get_session))->UserRead:
    
    return create_user_service(user,session)


@userrouter.get('/getall',response_model=list[UserRead])
def get_all_user(session: Session=Depends(get_session))->list[UserRead]:
    return get_all_user_service(session)

@userrouter.get('/{userid}',response_model=UserRead)
def get_user_by_id(userid:str,session: Session=Depends(get_session))->UserRead:
    return getuserby_id(userid,session)


@userrouter.patch('/{userid}',response_model=UserRead)
def update_user_by_id(userid:str,user:UserUpdate,session: Session=Depends(get_session))->UserRead:
    return updateuserby_id(userid,user,session)

@userrouter.delete('/{userid}')
def delete_by_id(userid:str,session: Session=Depends(get_session))->User:
    return deleteuserby_id(userid,session)

@userrouter.get("/{userid}/task",response_model=UserWithTasks)
def user_tasks(userid:str,session: Session=Depends(get_session))->UserWithTasks:
    return getting_user_tasks(userid,session)


@userrouter.post('/login',response_model=UserRead)
def login_user(user:UserLogin,session: Session=Depends(get_session))->UserRead:
    return login_user_service(user,session)