from fastapi import FastAPI
from routers import user, token, article
from database import database, metadata, engine, server

app = FastAPI()

app.include_router(token.router)
app.include_router(user.router)
app.include_router(article.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    server.stop()
