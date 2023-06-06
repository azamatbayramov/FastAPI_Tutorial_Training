from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

users = {
    "admin": "admin",
    "cat": "meow"
}


def check_user(username: str, password: str):
    if users.get(username) != password:
        raise HTTPException(401)
    return {
        "username": username,
        "password": password
    }


def logging(user_info: Annotated[dict, Depends(check_user)]):
    print(user_info)


@app.get("/", dependencies=[Depends(check_user), Depends(logging)])
def index():
    return "Hello, user!"
