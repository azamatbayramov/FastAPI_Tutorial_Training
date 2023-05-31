from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", response_model=None)
def index(meme: bool = True) -> Response | dict:
    if meme:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Welcome h-o-o-o-me!"}
