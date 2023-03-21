from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, CHAR, DATE
from database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(VARCHAR(50), nullable=False)
    gender = Column(VARCHAR(1), nullable=False)
    birth_date = Column(DATE, nullable=False)
    password = Column(CHAR(60), nullable=False)
