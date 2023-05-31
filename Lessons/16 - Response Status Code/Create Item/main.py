from fastapi import FastAPI, status

app = FastAPI()


@app.put("/items", status_code=status.HTTP_201_CREATED)
def create_item(name: str, price: float, country: str | None = None):
    return {"name": name, "price": price, "country": country} if country is not None else {"name": name, "price": price}
