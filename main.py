from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, test: Optional[str] = None):
    return {"item_id": item_id, "test": test}

@app.get("/nicholas")
def read_root():
    return {"Name": "Nicholas"}

# Sarina - testing adding changes to main using branch
