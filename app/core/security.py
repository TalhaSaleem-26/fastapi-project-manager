from pwdlib import PasswordHash
from jose import jwt
from datetime import datetime
from datetime import timedelta


from app.config import SECRET_KEY,ALGORITHM
password_hash = PasswordHash.recommended()




def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    exp = datetime.now() + timedelta(minutes=30)
    to_encode["exp"] = exp

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
    return encoded_jwt
