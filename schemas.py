import datetime
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    body: str
    create_date: str


class CreateArticle(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    gender: str
    birth_date: datetime.date | None = None

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str


class User(UserBase):
    id: int
    articles = list[Article] = []

    class Config:
        orm_mode = True
