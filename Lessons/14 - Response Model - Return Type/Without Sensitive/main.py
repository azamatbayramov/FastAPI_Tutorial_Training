import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class UserWithoutSensitiveInfo(BaseModel):
    username: str
    city: str


class UserWithSensitiveInfo(UserWithoutSensitiveInfo):
    password: str
    secret_word: str


app = FastAPI()


@app.post("/user")
def post_user(user: UserWithSensitiveInfo) -> UserWithoutSensitiveInfo:
    return user
