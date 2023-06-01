from fastapi import FastAPI, HTTPException, Path, status, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from typing import Annotated
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

items = [
    "Hello!",
    "Hey!",
    "Whasap!"
]


class ItemNotFoundException(Exception):
    def __init__(self, name):
        self.name = name


@app.exception_handler(ItemNotFoundException)
def item_not_found_exception_handler(request: Request, e: ItemNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "message": f"Oops! There is no item with id {e.name}"
        }
    )


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(request: Request, e: RequestValidationError):
    print("OMG! VALIDATION ERROR! IT IS NOT TRAINING! CLIENT SEND INVALID DATA!")
    return await request_validation_exception_handler(request, e)


@app.exception_handler(StarletteHTTPException)
def http_exception_handler(request: Request, e: StarletteHTTPException):
    return PlainTextResponse("Some error!", e.status_code)


@app.get("/items/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=0)]):
    if item_id > len(items) - 1:
        raise ItemNotFoundException(item_id)
    if item_id == 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No-no-no!")
    return items[item_id]
