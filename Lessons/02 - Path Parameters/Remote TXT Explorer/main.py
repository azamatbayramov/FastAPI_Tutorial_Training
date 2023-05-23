from fastapi import FastAPI
import os.path

app = FastAPI()


@app.get("/files/{file_path:path}")
def handler(file_path: str):
    if not file_path.endswith(".txt"):
        return "Error: File should be txt format."

    if not os.path.exists(file_path):
        return "Error: File not found"

    with open(file_path, "r") as file:
        return {"file_content": file.read()}
