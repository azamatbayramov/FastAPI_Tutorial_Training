from fastapi import FastAPI
from pydantic import BaseModel


class TwoVectorRequestBody(BaseModel):
    v1: list[int]
    v2: list[int]


app = FastAPI()


@app.get("/dot_product")
def get_dot_product(request_body: TwoVectorRequestBody):
    if len(request_body.v1) != len(request_body.v2):
        return "Error: vectors lists should be the same length"

    return sum([request_body.v1[i] * request_body.v2[i] for i in range(len(request_body.v1))])
