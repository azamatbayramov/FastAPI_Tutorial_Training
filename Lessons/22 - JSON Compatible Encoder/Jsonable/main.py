from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    creation_dt: datetime


items = []
app = FastAPI()


@app.post("/items")
def add_item(item: Item):
    items.append(jsonable_encoder(item))
    return items[-1]
