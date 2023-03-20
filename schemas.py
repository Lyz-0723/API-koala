import datetime
from pydantic import BaseModel


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
