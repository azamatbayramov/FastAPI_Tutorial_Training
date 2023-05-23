from fastapi import FastAPI

app = FastAPI()
request_counter = 0


@app.get("/count")
def increase_counter():
    global request_counter
    request_counter += 1
    return request_counter


@app.get("/reset")
def reset_counter():
    global request_counter
    request_counter = 0
    return request_counter
