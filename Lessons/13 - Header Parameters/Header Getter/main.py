from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()


@app.get("/header")
def get_header(
        accept: Annotated[str | None, Header()] = None,
        user_agent: Annotated[str | None, Header()] = None
):
    return {
        "accept": accept,
        "User-Agent": user_agent
    }
