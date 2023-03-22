from fastapi import FastAPI
from routers import user, token, article
from database import database, metadata, engine, server

app = FastAPI()

metadata.create_all(engine)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(article.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    server.stop()
