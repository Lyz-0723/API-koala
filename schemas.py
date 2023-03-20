from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    gender: str
    birth_date: str


class CreateUser(UserBase):
    password: str


class User(UserBase):
    id: int
