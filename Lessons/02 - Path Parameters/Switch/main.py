from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class State(str, Enum):
    ON = "on"
    OFF = "off"


turned_on: State = State("off")


@app.put("/turn/{state}")
def turn(state: State):
    global turned_on
    turned_on = state
    return {"state": turned_on}


@app.get("/state")
def get_state():
    return {"state": turned_on}
