import datetime
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class CreateArticle(ArticleBase):
    created_time: datetime.datetime | None = None
    creator_id: int


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
    articles: list[Article] = []
