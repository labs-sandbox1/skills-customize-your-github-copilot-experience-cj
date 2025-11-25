# Starter code for FastAPI REST API assignment
# Run: uvicorn starter-code:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: str = ""

# In-memory data store
items = [
    Item(id=1, name="Sample Item", description="This is a sample item.")
]

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items", response_model=Item)
def add_item(item: Item):
    items.append(item)
    return item
