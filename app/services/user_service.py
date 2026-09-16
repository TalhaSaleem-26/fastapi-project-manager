from app.models.user import User
from fastapi import HTTPException
from sqlmodel import Session , select
from app.schemas.user import UserCreate,UserRead,UserUpdate,UserWithTasks ,UserLogin
from app.core.security import hash_password , verify_password
from app.repositories.user_repositories import create_user_repository,find_user_by_username,get_all_user_repository,find_user_by_id,updateuser_data,delete_by_id ,getuserby_email
def create_user_service(user: UserCreate , session: Session)->UserRead:
    hashpassword=hash_password(user.password)
    newuser=User(
        username=user.username,
        email=user.email,
        password=hashpassword
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
    
    
def login_user_service(user:UserLogin,session: Session)->UserRead:
    Loginuser=getuserby_email(user.email ,session)
    
    if not Loginuser:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )
    
    verified=verify_password(user.password,Loginuser.password)
    
    if not verified :
        raise HTTPException(
            status_code=400,
            detail='Password Doesnot Match'
        )
    
    
    else :
        
        return Loginuser