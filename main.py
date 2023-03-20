from fastapi import FastAPI
from routers import user
from database import engine
import models


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
