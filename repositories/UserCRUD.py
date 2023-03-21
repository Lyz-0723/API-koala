from models import User
import schemas
from database import database
from authentication import hashing


async def get_all_users():
    query = User.select()
    return await database.fetch_all(query)


async def get_specific_user(user_id: int):
    query = User.select().where(User.c.id == user_id)
    return await database.fetch_one(query)


async def get_specific_user_by_name(user_name: str):
    query = User.select().where(User.c.name == user_name)
    return await database.fetch_one(query)


async def create_user(user: schemas.CreateUser):
    query = User.insert().values(name=user.name,
                                 gender=user.gender,
                                 birth_date=user.birth_date,
                                 password=hashing.get_password_hash(user.password))
    await database.execute(query)
    return user


async def delete_user(user_id: int):
    query = User.delete().where(User.c.id == user_id)
    await database.execute(query)
    return {"User deletion done"}
