from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()


@app.get("/root/{number}")
def get_root(
        number: Annotated[float, Path(ge=0, title="Number", description="Number for getting root")],
        degree: Annotated[float, Query(gt=0, title="Degree", description="Degree of root")] = 2
):
    return number ** (1 / degree)
