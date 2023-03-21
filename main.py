from fastapi import FastAPI
from routers import user, token
from database import engine
import models


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(token.router)
app.include_router(user.router)
