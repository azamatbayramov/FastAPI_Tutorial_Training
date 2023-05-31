from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


@app.post("/upload_file")
def upload_file(name: Annotated[str, Form()], file: UploadFile):
    filename_in_system = f"{name}_{file.filename}"
    open(filename_in_system, "wb").write(file.file.read())
    return {
        "filename_in_system": filename_in_system
    }


@app.get("/")
def index():
    content = """
        <body>
            <form action="/upload_file" enctype="multipart/form-data" method="post">
                <input name="name" type="string">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    """
    return HTMLResponse(content=content)
