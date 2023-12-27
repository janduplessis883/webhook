from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    user_id: int

app = FastAPI()

@app.post("/webhook")
def read_item(item: Item):
    print(item)
    return item

# uvicorn main:app --reload  #nRUnniing this locally