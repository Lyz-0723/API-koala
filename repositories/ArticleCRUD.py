import datetime

from models import Article
from database import database
import schemas


async def get_all_articles():
    query = Article.select()
    return await database.fetch_all(query)


async def get_specific_article(article_id: int):
    query = Article.select().where(Article.c.id == article_id)
    return await database.fetch_one(query)


async def create_article(article: schemas.ArticleBase, creator: schemas.User):
    query = Article.insert().values(title=article.title,
                                    body=article.body,
                                    created_time=datetime.datetime.now(),
                                    creator_id=creator.id)
    await database.execute(query)
    return article


async def delete_article(article_id: int):
    query = Article.select().where(Article.c.id == article_id)
    await database.execute(query)
    return {"Article deletion done"}
