from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()


def get_user(username: str, password: str) -> str | None:
    if username == "admin" and password == "admin":
        return "admin"
    elif username == "cat" and password == "meow":
        return "cat"
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


UsernameDependence = Annotated[str | None, Depends(get_user)]


@app.get("/")
def index(username: UsernameDependence) -> str:
    return f"Hey, {username}"


@app.get("/text")
def get_work(username: UsernameDependence) -> str:
    return "Some text here"
