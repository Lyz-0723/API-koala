from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas
from ../repositories import UserCRUD

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


# Getting the information of all users
@router.get("/", response_model=schemas.ShowUser)
def get_all_users(db: Session = Depends(database.get_db)):
    return UserCRUD.get_all_users(db)


# Getting the information of specific users using "id"
@router.get("/{id}", response_model=schemas.ShowUser)
def get_specific_users(user_id, db: Session = Depends(database.get_db)):
    return UserCRUD.get_specific_users(user_id, db)


# Creating a user with
@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_users(user: schemas.User, db: Session = Depends(database.get_db)):
    return UserCRUD.create_user(user, db)

