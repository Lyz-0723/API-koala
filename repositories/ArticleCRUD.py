import datetime

from sqlalchemy.orm import Session
import models
import schemas


def get_all_articles(db: Session):
    return db.query(models.Article).all()


def create_article(article: schemas.ArticleBase, db: Session):
    new_article = models.Article(title=article.title,
                                 body=article.body,
                                 created_time=datetime.datetime.now(),
                                 creator_id=51)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
