from fastapi import FastAPI
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(description="Name(maybe full name)")
    grades: list[int] = Field(description="List of grades", ge=2, le=5)


class RequestBody(BaseModel):
    users: list[User] = Field(description="List of users for calculating GPA")


app = FastAPI()


@app.post("/calculate")
def calculate_gpa(body: RequestBody):
    answer = []
    for user in body.users:
        gpa = sum(user.grades) / len(user.grades)
        answer.append({
            "user": user,
            "gpa": gpa
        })

    return answer
