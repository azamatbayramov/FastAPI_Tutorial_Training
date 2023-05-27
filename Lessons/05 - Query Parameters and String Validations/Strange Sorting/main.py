from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/sort")
def get_sort(
        lst: Annotated[list[int], Query(title="List for sorting", description="List of integers for sorting")],
        reverse: bool = False
):
    return sorted(lst, reverse=reverse)
