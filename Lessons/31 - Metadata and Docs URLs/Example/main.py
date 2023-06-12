from fastapi import FastAPI

app = FastAPI(
    title="Best API",
    description="API for _all_ your **purposes**",
    version="1.2.1",
    contact={
        "name": "Azamat Bayramov",
        "url": "https://t.me/azamatbayramov",
        "email": "bayramov.azamat04@gmail.com"
    },
    docs_url="/swagger",
    redoc_url=None,
    openapi_tags=[
        {
            "name": "Main",
            "description": "Main endpoints"
        },
        {
            "name": "Users",
            "description": "Endpoints for users",
            "externalDocs": {
                "description": "Docs: How to talk to people?",
                "url": "https://www.wikihow.com/Talk-to-People"
            }
        },
        {
            "name": "Items",
            "description": "Endpoints for items",
            "externalDocs": {
                "description": "Docs: How to talk to items?",
                "url": "https://example.com"
            }
        }
    ],
    openapi_url="/api/v1/openapi.json"
)


@app.get("/", tags=["Main"])
def index():
    return {"Hello, world!"}


@app.get("/users/", tags=["Users"])
def get_users():
    return []


@app.post("/users/", tags=["Users"])
def post_user():
    return "OK"


@app.get("/items/", tags=["Items"])
def get_items():
    return []


@app.post("/items/", tags=["Items"])
def post_items():
    return "OK"
