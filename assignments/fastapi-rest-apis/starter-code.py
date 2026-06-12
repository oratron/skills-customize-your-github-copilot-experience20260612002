from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

items: List[Item] = [
    Item(id=1, name="Notebook", description="A ruled notebook", price=4.99),
    Item(id=2, name="Pen", description="A blue ink pen", price=1.99),
]

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    new_id = max(item.id for item in items) + 1 if items else 1
    new_item = Item(id=new_id, **item.model_dump())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: ItemCreate):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = Item(id=item_id, **updated_item.model_dump())
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")
