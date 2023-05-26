from fastapi import FastAPI

app = FastAPI()


@app.get("/sequence")
def get_sequence(start: int = 0, length: int = 10, step: int = 1):
    return list(range(start, start + length * step, step))
