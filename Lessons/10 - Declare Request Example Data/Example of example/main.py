from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    rating: int

    class Config:
        schema_extra = {
            "example": {
                "id": 12,
                "name": "Andrew",
                "rating": 154
            }
        }


app = FastAPI()


@app.post("/user")
def post_user(user: User):
    return "OK"
