from fastapi import FastAPI
from routers import user, token, article
from database import engine
import models


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(token.router)
app.include_router(user.router)
app.include_router(article.router)
