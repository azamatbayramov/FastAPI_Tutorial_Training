from fastapi import FastAPI, Path, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated


class Item(BaseModel):
    name: str
    price: float
    desc: str | None


class ItemForPatch(BaseModel):
    name: str | None = None
    price: float | None = None
    desc: str | None = None


class ItemWithID(BaseModel):
    item_id: int
    item: Item


app = FastAPI()
items_count = 0
items = {}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def get_item(item_id: Annotated[int, Path(ge=1)]):
    if items.get(item_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return items[item_id]


@app.post("/items", response_model=ItemWithID, response_model_exclude_unset=True)
def post_item(item: Item):
    global items_count
    items_count += 1

    items[items_count] = jsonable_encoder(item)

    return {
        "item_id": items_count,
        "item": items[items_count]
    }


@app.put("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def put_item(item_id: Annotated[int, Path(ge=1)], item: Item):
    if items.get(item_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    items[item_id] = jsonable_encoder(item)

    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def patch_item(item_id: Annotated[int, Path(ge=1)], item: ItemForPatch):
    if items.get(item_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    stored_items_data = items[item_id]
    stored_item_model = Item(**stored_items_data)
    update_data = item.dict(exclude_unset=True)
    update_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(update_item)

    return items[item_id]


@app.delete("/items/{item_id}")
def delete_item(item_id: Annotated[int, Path(ge=1)]):
    if items.get(item_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    items[item_id] = None
