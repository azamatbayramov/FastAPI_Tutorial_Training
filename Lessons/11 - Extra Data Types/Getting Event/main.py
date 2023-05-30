from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Event(BaseModel):
    id: UUID
    name: str
    start_at: datetime
    finish_at: datetime


app = FastAPI()


@app.put("/event")
def put_event(event: Event):
    return "OK"
