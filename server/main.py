from fastapi import FastAPI
from database import init_db

import os
import openai
openai.api_key = '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'
import models
from pydantic import BaseModel


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

class prompt(BaseModel):
    content: str
@app.post("/api/safe")
async def get_activities(prompt: prompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt.content}
        ]
    )
    return completion.choices[0].message.content