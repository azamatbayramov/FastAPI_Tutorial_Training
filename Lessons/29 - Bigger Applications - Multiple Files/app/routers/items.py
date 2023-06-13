from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from .. import crud, models, schemas
from ..database import SessionLocal, engine, get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get("/")
def get_items(db: Annotated[Session, Depends(get_db)], skip: int = 0, limit: int = 10):
    items = crud.get_items(db, skip, limit)
    return items


@router.post("/", response_model=schemas.Item)
def create_item_for_user(db: Annotated[Session, Depends(get_db)], user_id: int, item: schemas.ItemCreate):
    return crud.create_user_item(db, item, user_id)
