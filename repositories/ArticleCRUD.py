import datetime

from sqlalchemy.orm import Session
import models
import schemas


def get_all_articles(db: Session):
    return db.query(models.Article).all()


def get_specific_article(article_id: int, db: Session):
    return db.query(models.Article).filter_by(id=article_id).first()


def create_article(article: schemas.ArticleBase, creator: schemas.User, db: Session):
    new_article = models.Article(title=article.title,
                                 body=article.body,
                                 created_time=datetime.datetime.now(),
                                 creator_id=creator.id)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def delete_article(article_id: int, db: Session):
    db.query(models.Article).filter_by(id=article_id).delete(synchronize_session=False)
    db.commit()
    return {"Article deletion done"}
