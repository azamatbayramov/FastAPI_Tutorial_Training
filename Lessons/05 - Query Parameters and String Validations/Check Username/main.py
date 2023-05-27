from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/check_username")
def check_username(username: Annotated[str | None, Query(max_length=20, min_length=3)] = ...):
    return username
