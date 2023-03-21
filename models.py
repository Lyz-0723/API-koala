import sqlalchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, CHAR, DATE, DATETIME
from sqlalchemy.orm import relationship
from database import metadata


User = sqlalchemy.Table(
    "Users",
    metadata,
    Column("id", sqlalchemy.INTEGER, primary_key=True, index=True),
    Column("name", sqlalchemy.VARCHAR(50), nullable=False),
    Column("gender", sqlalchemy.VARCHAR(1), nullable=False),
    Column("birth_date", sqlalchemy.DATE, nullable=False),
    Column("password", sqlalchemy.CHAR(60), nullable=False),
)

Article = sqlalchemy.Table(
    "Articles",
    metadata,
    Column("id", sqlalchemy.INTEGER, primary_key=True, index=True),
    Column("title", sqlalchemy.VARCHAR(50), nullable=False),
    Column("body", sqlalchemy.VARCHAR(600), nullable=False),
    Column("created_time", sqlalchemy.DATETIME, nullable=False),
    Column("creator_id", INTEGER, ForeignKey("Users.id"))
)
