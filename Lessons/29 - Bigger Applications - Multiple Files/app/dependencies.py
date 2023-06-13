from typing import Annotated

from fastapi import Header, HTTPException


def get_special_header(x_token: Annotated[str, Header()]):
    if x_token != "super_secret_fake_token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


def get_special_query(token: str):
    if token != "special_query_token":
        raise HTTPException(status_code=400, detail="Query token invalid")
