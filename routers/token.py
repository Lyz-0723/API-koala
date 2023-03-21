from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from ..authentication import security
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

import database
import models

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/token")
def token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter_by(name=request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not security.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    access_token = security.create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}
