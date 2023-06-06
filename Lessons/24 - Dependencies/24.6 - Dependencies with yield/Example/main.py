from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated


def dep1(hey: str):
    if hey == "ya":
        raise HTTPException(400, "ya?")
    print("Dep1 starts")
    try:
        yield "dep1"
    finally:
        print("Dep1 stops")


def dep2(dep1: Annotated[str, Depends(dep1)]):
    print("Dep2 starts")
    try:
        yield "dep2"
    finally:
        print("Dep2 stops")


def dep3(dep1: Annotated[str, Depends(dep1)], dep2: Annotated[str, Depends(dep2)]):
    print("Dep3 starts")
    try:
        yield "dep3"
    finally:
        print("Dep3 stops")


app = FastAPI()


@app.get("/")
def index(dep: Annotated[str, Depends(dep3)]):
    return dep
