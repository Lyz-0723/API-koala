import datetime
from pydantic import BaseModel
from typing import Union


class ArticleBase(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class CreateArticle(ArticleBase):
    created_time: Union[datetime.datetime, None] = None
    creator_id: int


class Article(ArticleBase):
    article_id: int


class UserBase(BaseModel):
    name: str
    gender: str
    birth_date: Union[datetime.date, None] = None

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str


class User(UserBase):
    user_id: int
    articles: list[Article] = []
