from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import database
import schemas
from repositories import UserCRUD

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


# Getting the information of all users
@router.get("/", response_model=list[schemas.UserBase])
def get_all_users(db: Session = Depends(database.get_db)):
    return UserCRUD.get_all_users(db)


# Getting the information of specific users using "id"
@router.get("/{id}", response_model=schemas.UserBase)
def get_specific_user(user_id, db: Session = Depends(database.get_db)):
    return UserCRUD.get_specific_user(user_id, db)


# Creating a user with
@router.post("/", response_model=schemas.CreateUser, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.CreateUser, db: Session = Depends(database.get_db)):
    return UserCRUD.create_user(user, db)
