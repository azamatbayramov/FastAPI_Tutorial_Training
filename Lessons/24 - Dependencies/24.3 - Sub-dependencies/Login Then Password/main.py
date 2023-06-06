from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

users = {
    "admin": "admin",
    "cat": "meow"
}


def get_username(username: str):
    if users.get(username) is None:
        raise HTTPException(401, "There is no such login")

    return username


class User:
    def __init__(self, username: Annotated[str, Depends(get_username)], password: str):
        if users.get(username) != password:
            raise HTTPException(401, "Password is incorrect")

        self.username = username
        self.password = password


@app.get("/")
def index(user: Annotated[User, Depends()]):
    return f"Hello, {user.username} with password {user.password}!"
