
from fastapi import FastAPI

app = FastAPI(title="DevOps Demo API")


@app.get("/")
def root():
    return {
        "message": "Hello, DevOps!",
        "version": "1.0.2",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Item {item_id}",
    }
