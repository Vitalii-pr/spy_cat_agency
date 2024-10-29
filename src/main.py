from fastapi import FastAPI
from .cat import models

from .database import engine

from .cat.routers import cats_router

from .missions_and_targets.router import mission_router

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router=cats_router, prefix="/spy_cats")
app.include_router(router=mission_router, prefix="/missions")
