from sqlalchemy.orm import Session
import models
import schemas
from authentication import hashing


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_specific_user(user_id: int, db: Session):
    return db.query(models.User).filter_by(id=user_id).first()


def get_user_by_name(name: str, db: Session):
    return db.query(models.User).filter_by(name=name).first()


def create_user(user: schemas.CreateUser, db: Session):
    new_user = models.User(name=user.name,
                           gender=user.gender,
                           birth_date=user.birth_date,
                           password=hashing.get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    return new_user


def delete_user(user_id: int, db: Session):
    db.query(models.User).filter_by(id=user_id).delete(synchronize_session=False)
    db.commit()
    return {"User deletion done"}
