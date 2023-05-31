from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()


@app.post("/login")
def login(username: Annotated[str, Form()], password: Annotated[str, Form()]) -> str:
    if username == "admin" and password == "admin":
        return "OK"
    return "Authentication Error"
