from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Annotated


class Item(BaseModel):
    id: int
    name: str
    price: float


class User(BaseModel):
    id: int
    name: str
    address: str


app = FastAPI()


@app.post("/create_receipt")
def create_receipt(
        item: Annotated[Item, Body(description="Information about item")],
        user: Annotated[User, Body(description="Information about user")],
        count: Annotated[int, Body(description="Number of pieces", ge=1)],
        delivery_cost: Annotated[float, Body(description="Delivery cost", ge=0)]
):
    return {
        "item": item,
        "user": user,
        "count": count,
        "delivery_cost": delivery_cost,
        "total": count * item.price + delivery_cost
    }
