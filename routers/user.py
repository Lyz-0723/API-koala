from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database
import schemas
from repositories import UserCRUD

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


# Getting the information of all users
@router.get("/")
def get_all_users(db: Session = Depends(database.get_db)) -> list[schemas.UserBase]:
    return UserCRUD.get_all_users(db)


# Getting the information of specific users using "id"
@router.get("/{id}")
def get_specific_user(user_id, db: Session = Depends(database.get_db)) -> schemas.UserBase:
    db_user = UserCRUD.get_specific_user(user_id, db)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return db_user


# Creating a user
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser, db: Session = Depends(database.get_db)) -> schemas.CreateUser:
    db_user = UserCRUD.get_user_by_name(user.name, db)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username already registered")
    if user.gender != 'M' and user.gender != 'F':
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Gender should be M or F")
    return UserCRUD.create_user(user, db)
