from fastapi import FastAPI, Path, HTTPException, status
from enum import Enum
from pydantic import BaseModel
from typing import Annotated


class Tags(Enum):
    items = "Items"
    users = "Users"


class Item(BaseModel):
    name: str
    price: float
    description: str | None


class User(BaseModel):
    username: str
    password: str
    full_name: str | None


class UserOut(BaseModel):
    username: str
    full_name: str | None


app = FastAPI()
users = [
    User(username="admin", password="admin"),
    User(username="alice", password="qwerty"),
    User(username="bob", password="AndersonPasswordBob", full_name="Bob Anderson")
]
items = [
    Item(name="Apple", price=40),
    Item(name="Bread", price=13, description="Made in Earth")
]


@app.get(
    "/users/{user_id}",
    response_model=UserOut,
    tags=[Tags.users],
    response_model_exclude_unset=True,
    summary="Get the user",
    description="More descriptional summary, hehe"
)
def get_user(user_id: Annotated[int, Path(ge=0)]):
    if user_id >= len(users):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return users[user_id]


@app.post(
    "/users",
    response_model=UserOut,
    tags=[Tags.users],
    summary="Create a user",
    description="More descriptional summary, hehe"
)
def post_user(user: User):
    users.append(user)
    return user


@app.get("/elems/{item_id}", deprecated=True, tags=[Tags.items])
@app.get(
    "/items/{item_id}",
    response_model=Item,
    tags=[Tags.items],
    response_model_exclude_unset=True,
    summary="Get the item",
    description="More descriptional summary, hehe"
)
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return items[item_id]


@app.post(
    "/items",
    response_model=Item,
    tags=[Tags.items],
    summary="Create an item",
    response_description="Description of response here should be but I am too lazy but not lazy to write this long text"
)
def post_item(item: Item):
    """
    Create an item with all the information:

    - **name**: name of the item
    - **price**: price of the item
    - **description**: description of the item(optional)
    """
    items.append(item)
    return item
