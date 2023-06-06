from fastapi import Depends, FastAPI
from typing import Annotated, Any


class MyContextManager:
    def __init__(self, n):
        self.n = n
        print(f"Dep{self.n} initialized")

    def __enter__(self):
        print(f"Dep{self.n} entered")
        return self.n

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Dep{self.n} exited")

    def __repr__(self):
        return f"dep{self.n}"

    def __str__(self):
        return self.__str__()


def dep1():
    with MyContextManager(1) as dep11:
        print(dep11)
        yield dep11


app = FastAPI()


@app.get("/")
def index(dep11: Annotated[Any, Depends(dep1)]):
    print(dep11)
    return dep11
