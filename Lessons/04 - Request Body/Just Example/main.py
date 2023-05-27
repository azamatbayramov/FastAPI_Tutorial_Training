from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    full_name: str
    address: str


class Item(BaseModel):
    id: int
    name: str
    price: int


app = FastAPI()

items: list[Item] = [
    Item(id=0, name="Apple", price=30),
    Item(id=1, name="Juice", price=40),
    Item(id=2, name="Bread", price=20),
    Item(id=3, name="Pasta", price=50),
]


@app.post("/buy/{item_id}")
def buy(item_id: int, user: User, count: int = 1):
    item_list = [item for item in items if item.id == item_id]
    item = item_list[0] if len(item_list) != 0 else None

    if item is None:
        return "Error: Not Found"

    receipt = {
        "item": item,
        "user": user,
        "total": item.price * count
    }

    return receipt
