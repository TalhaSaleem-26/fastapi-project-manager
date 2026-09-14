from sqlmodel import Session , select
from app.schemas.user import UserUpdate

from app.models.user import User
def create_user_repository(user:User,session:Session)->User:
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user


def find_user_by_username(username: str, session: Session) -> User | None:
    statement = select(User).where(User.username == username)
    query = session.exec(statement).first()

    return query

def get_all_user_repository(session: Session)->list[User]:
    statement=select(User)
    query=session.exec(statement).all()
    return query

def find_user_by_id(userid:str,session: Session)->User|None:
    statement=select(User).where(User.id==userid)
    query=session.exec(statement).first()
    return query

def updateuser_data(userid:str,user:UserUpdate,session: Session)->User|None :
    statement=select(User).where(User.id==userid)
    query=session.exec(statement).first()
    
    if not query :
        return None
    
    update_values=user.model_dump(exclude_unset=True)
    
    for field , value in update_values.items():
        setattr(query , field,value)
        
    session.add(query)
    session.commit()
    session .refresh(query)
    
    return query
    
    
def delete_by_id(userid:str,session: Session)->User|None:
    statement=select(User).where(User.id==userid)
    query=session.exec(statement).first()
    
    if(query):
        session.delete(query)
        session.commit()
        
        return query
    
    else :
        return None
    
    session.delete(query)
    
    
