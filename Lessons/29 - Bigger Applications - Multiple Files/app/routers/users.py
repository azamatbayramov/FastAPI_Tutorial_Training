from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from .. import crud, models, schemas
from ..database import SessionLocal, engine, get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}", response_model=schemas.User, tags=["Users"])
def get_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[schemas.User], tags=["Users"])
def get_users(db: Annotated[Session, Depends(get_db)], skip: int = 0, limit: int = 10):
    users = crud.get_users(db, skip, limit)
    return users


@router.post("/", response_model=schemas.User, tags=["Users"])
def post_user(db: Annotated[Session, Depends(get_db)], user: schemas.UserCreate):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    return crud.create_user(db, user)
