from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, CHAR, DATE, DATETIME
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(VARCHAR(50), nullable=False)
    gender = Column(VARCHAR(1), nullable=False)
    birth_date = Column(DATE, nullable=False)
    password = Column(CHAR(60), nullable=False)

    articles = relationship("Article", back_populates="creator")


class Article(Base):
    __tablename__ = "Articles"
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(VARCHAR(50), nullable=False)
    body = Column(VARCHAR(600), nullable=False)
    created_time = Column(DATETIME, nullable=False)
    creator_id = Column(INTEGER, ForeignKey("Users.id"))

    creator = relationship("User", back_populates="articles")
