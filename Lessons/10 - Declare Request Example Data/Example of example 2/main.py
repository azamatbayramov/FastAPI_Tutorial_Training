from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated


class User(BaseModel):
    id: int
    name: str
    rating: int


app = FastAPI()


@app.post("/user")
def post_user(user: Annotated[User, Body(example={
    "id": 12,
    "name": "Andrew",
    "rating": 154
})]):
    return "OK"
