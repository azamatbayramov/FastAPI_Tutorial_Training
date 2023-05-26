from fastapi import FastAPI

app = FastAPI()


@app.get("/inverse")
def inverse(string: str):
    return string[::-1]
