import datetime

from models import Article
from database import database
import schemas


async def get_all_articles():
    query = Article.select()
    articles = await database.fetch_all(query)
    return articles


async def get_specific_article(article_id: int):
    query = Article.select().where(Article.c.id == article_id)
    return await database.fetch_one(query)


async def create_article(article: schemas.ArticleBase, creator: schemas.User):
    now = datetime.datetime.now()
    query = Article.insert().values(title=article.title,
                                    body=article.body,
                                    created_time=now,
                                    creator_id=creator.id)
    await database.execute(query)

    result = {**article.dict(), "created_time": now, "creator_id": creator.id}
    return result


async def delete_article(article_id: int):
    query = Article.delete().where(Article.c.id == article_id)
    await database.execute(query)
    return {"Article deletion done"}
