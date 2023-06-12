import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def calculate_processing_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    processing_time = time.time() - start_time
    response.headers["X-Processing-Time"] = str(processing_time)
    return response
