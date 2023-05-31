from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    description: str = "description"
    importer: str = "importer"


items = [
    {
        "name": "Apple",
        "price": 40.1
    },
    {
        "name": "Bread",
        "price": 13.42,
        "importer": "Tatarstan"
    },
    {
        "name": "CPU",
        "price": 2000,
        "importer": "Ufa",
        "description": "description"
    }
]

app = FastAPI()


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def get_item(item_id: int):
    return items[item_id]
