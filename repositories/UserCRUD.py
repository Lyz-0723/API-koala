from sqlalchemy.orm import Session
import models, schemas


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
                           password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
