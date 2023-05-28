from fastapi import FastAPI
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(description="Id of the user", ge=1)
    name: str = Field(description="Name of the user", min_length=1, max_length=30)
    surname: str | None = Field(description="Surname of the user", default=None, max_length=30)
    email: str | None = Field(description="Email address of the user", default=None, max_length=100)


app = FastAPI()


@app.post("/user")
def edit_user(user: User):
    return "OK"
