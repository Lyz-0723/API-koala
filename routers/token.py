from datetime import timedelta
from typing import Annotated

from authentication import JWTtoken
import database

from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/token")
def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(database.get_db)):
    user = JWTtoken.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(days=JWTtoken.expire_days())
    access_token = JWTtoken.create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
