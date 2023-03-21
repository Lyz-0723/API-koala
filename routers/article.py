from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database
import schemas
from authentication.JWTtoken import get_current_user
from repositories import ArticleCRUD

router = APIRouter(
    prefix="/article",
    tags=["Article"]
)


# Getting the information of all articles
@router.get("/")
def get_all_articles(current_user: Annotated[schemas.User, Depends(get_current_user)],
                     db: Session = Depends(database.get_db)) -> list[schemas.Article]:
    return ArticleCRUD.get_all_articles(db)


# Creating an article
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleBase,
                   current_user: Annotated[schemas.User, Depends(get_current_user)],
                   db: Session = Depends(database.get_db)) -> schemas.CreateArticle:
    return ArticleCRUD.create_article(article, current_user, db)


# Deleting an article
@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_article(article_id: int,
                   current_user: Annotated[schemas.User, Depends(get_current_user)],
                   db: Session = Depends(database.get_db)):
    if not ArticleCRUD.get_specific_article(article_id, db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")

    if not current_user.id == ArticleCRUD.get_specific_article(article_id, db).creator_id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Article not belongs to the user")

    return ArticleCRUD.delete_article(article_id, db)
