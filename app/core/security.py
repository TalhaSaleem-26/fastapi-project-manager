from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.models.user import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.config import SECRET_KEY, ALGORITHM
from app.db.session import get_session
from app.repositories.user_repositories import find_user_by_id


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")
password_hash = PasswordHash.recommended()




def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    exp = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode["exp"] = exp

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = find_user_by_id(user_id, session)

    if user is None:
        raise credentials_exception

    return user

def auth_admin(currentuser: User = Depends(get_current_user)) -> User:
    if currentuser.role == "admin":
        return currentuser

    raise HTTPException(
        status_code=403,
        detail="Unauthorized access"
    )