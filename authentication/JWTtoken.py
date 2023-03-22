# Creating JWT token and verifying users
from datetime import timedelta, datetime
from typing import Annotated

from repositories import UserCRUD
from authentication import hashing
from authentication import oauth2

from pydantic import BaseModel
from jose import jwt, JWTError
from fastapi import Depends, status, HTTPException

ACCESS_TOKEN_EXPIRE_DAYS = 7
SECRET_KEY = "bf45828df107a8c13e2b1e902efbfac5c9edf497475607283964933ca8a40fb5"
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def expire_days():
    return ACCESS_TOKEN_EXPIRE_DAYS


async def authenticate_user(username: str, password: str):
    user = await UserCRUD.get_specific_user_by_name(username)
    if not user:
        return False
    if not hashing.verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2.oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await UserCRUD.get_specific_user_by_name(token_data.username)
    if user is None:
        raise credentials_exception
    return user
