from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException

import schemas
from authentication.JWTtoken import get_current_user
from repositories import ArticleCRUD

router = APIRouter(
    prefix="/article",
    tags=["Article"]
)


# Getting the information of all articles
@router.get("/")
async def get_all_articles(current_user: Annotated[schemas.User, Depends(get_current_user)]) -> list[schemas.Article]:
    return await ArticleCRUD.get_all_articles()


# Creating an article
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_article(article: schemas.ArticleBase,
                         current_user: Annotated[schemas.User, Depends(get_current_user)]) -> schemas.CreateArticle:
    return await ArticleCRUD.create_article(article, current_user)


# Deleting an article
@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_article(article_id: int,
                         current_user: Annotated[schemas.User, Depends(get_current_user)]):
    if not await ArticleCRUD.get_specific_article(article_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")

    if not current_user.user_id == (await ArticleCRUD.get_specific_article(article_id)).creator_id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Article not belongs to the user")

    return await ArticleCRUD.delete_article(article_id)
