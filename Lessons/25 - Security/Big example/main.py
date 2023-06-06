from typing import Annotated
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    token: str


@app.get("/my_token", response_model=Token)
def get_my_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {
        "token": token
    }
