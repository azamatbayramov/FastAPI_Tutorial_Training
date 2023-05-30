from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    username: str
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


app = FastAPI()
users = []


def fake_password_hash(password: str) -> str:
    return f"fake_hashed_[{password}]"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hash(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    users.append(user_in_db)
    return user_in_db


@app.put("/users", response_model=UserOut, response_model_exclude_defaults=True)
def put_user(user_in: UserIn):
    return fake_save_user(user_in)


@app.get("/users", response_model=Union[list[UserOut], dict[str, str]], response_model_exclude_defaults=True)
def get_users():
    if users:
        return users
    return {"message": "there is no users"}
