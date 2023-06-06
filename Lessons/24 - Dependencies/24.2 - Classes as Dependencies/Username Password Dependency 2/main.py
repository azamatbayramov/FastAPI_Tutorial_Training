from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

users = {
    "admin": "admin",
    "cat": "meow"
}


class User:
    def __init__(self, username: str, password: str):
        if users.get(username) != password:
            raise HTTPException(status_code=401)

        self.username = username
        self.password = password


UserDependency = Annotated[User, Depends()]


@app.get("/")
def index(user: UserDependency):
    return f"Hello, {user.username}!"


@app.get("/password")
def get_password(user: UserDependency):
    return f"{user.username}:{user.password}"
