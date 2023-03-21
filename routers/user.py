from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import schemas
from authentication.JWTtoken import get_current_user
from repositories import UserCRUD

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


# Getting the information of all users
@router.get("/")
def get_all_users(current_user: Annotated[schemas.User, Depends(get_current_user)]) -> list[schemas.UserBase]:
    return UserCRUD.get_all_users()


# Getting the information of specific users using "id"
@router.get("/{id}")
def get_specific_user(user_id,
                      current_user: Annotated[schemas.User, Depends(get_current_user)]) -> schemas.UserBase:
    db_user = UserCRUD.get_specific_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return db_user


# Creating a user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser) -> schemas.CreateUser:
    db_user = UserCRUD.get_specific_user_by_name(user.name)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username already registered")
    if user.gender != 'M' and user.gender != 'F':
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Gender should be M or F")
    return UserCRUD.create_user(user)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_user(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return UserCRUD.delete_user(current_user.id)
