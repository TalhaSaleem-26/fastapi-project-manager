from app.models.user import User
from fastapi import HTTPException
from sqlmodel import Session , select
from app.schemas.user import UserCreate,UserRead,UserUpdate,UserWithTasks
from app.repositories.user_repositories import create_user_repository,find_user_by_username,get_all_user_repository,find_user_by_id,updateuser_data,delete_by_id
def create_user_service(user: UserCreate , session: Session)->UserRead:
    newuser=User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    existing_user = find_user_by_username(user.username, session)

    if existing_user:
        raise HTTPException(status_code=400,
                    detail="user already Exist")
    

    return create_user_repository(newuser,session)


def get_all_user_service(session: Session)->list[User]:
   return get_all_user_repository(session)
   
def getuserby_id(userid:str,session: Session)->User:
    user=find_user_by_id(userid,session)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
        
    else :
        return user
    
def updateuserby_id(userid: str,user:UserUpdate,session: Session):
    user=updateuser_data(userid,user,session)
    if not user :
        raise HTTPException(
            status_code=404,
            detail="user not Found"
            )
        
    return user


def deleteuserby_id(userid:str,session: Session)->User:
    data= delete_by_id(userid,session)
    if not data:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
        
    else :
        return (
            data
            
        )
        
def getting_user_tasks(userid:str,session: Session)->UserWithTasks:
    user= getuserby_id(userid,session)
    return user
    
    