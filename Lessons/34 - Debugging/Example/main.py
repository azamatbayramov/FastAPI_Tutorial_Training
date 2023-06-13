from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/{a}/{b}")
def ab(a: int, b: int):
    return a + b


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
