from typing import Annotated
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    token: str


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token: str) -> User:
    return User(
        username=token + "_fake_decoded",
        email="john@example.com",
        full_name="John Doe"
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    return fake_decode_token(token)


@app.get("/me", response_model=User)
def get_my_token(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
