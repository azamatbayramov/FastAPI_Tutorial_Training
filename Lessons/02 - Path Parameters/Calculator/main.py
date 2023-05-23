from fastapi import FastAPI

app = FastAPI()


@app.get("/{a}/{op}/{b}")
def calculate(a: float, op: str, b: float):
    match op:
        case "plus":
            return a + b
        case "minus":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            if b == 0:
                return "Error: Division by zero is undefined"
            return a / b
        case _:
            return "Error: Unknown operator"
