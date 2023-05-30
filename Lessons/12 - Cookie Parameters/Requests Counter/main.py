from fastapi import FastAPI, Cookie, Response
from typing import Annotated

app = FastAPI()


@app.get("/count")
def get_count(response: Response, count: Annotated[int, Cookie()] = 0):
    count += 1
    response.set_cookie(key="count", value=str(count))
    return {"count": count}
