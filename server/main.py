from fastapi import FastAPI
from database import init_db

import models


app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    The `on_startup` function is called when the application starts up and it initializes the database.
    """
    init_db()


@app.get("/")
async def root():
    return {"message": "The API has started successfully"}