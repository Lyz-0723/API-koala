from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import database
import schemas
from repositories import ArticleCRUD

router = APIRouter(
    prefix="/article",
    tags=["Article"]
)


# Getting the information of all articles
@router.get("/")
def get_all_articles(db: Session = Depends(database.get_db)) -> list[schemas.ArticleBase]:
    return ArticleCRUD.get_all_articles(db)


# Creating an article
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleBase, db: Session = Depends(database.get_db)) -> schemas.CreateArticle:
    return ArticleCRUD.create_article(article, db)
