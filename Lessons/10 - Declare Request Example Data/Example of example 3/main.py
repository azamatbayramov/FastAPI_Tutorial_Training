from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated


class User(BaseModel):
    id: int = Field(example=12)
    name: str = Field(example="Andrew")
    rating: int = Field(example=154)


app = FastAPI()


@app.post("/user")
def post_user(user: User):
    return "OK"
