from typing import Union
import model
from model import Comment,TextRequest
from fastapi import FastAPI

app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict")
async def predict(text_request: Comment):
    prediction = text_request.content
    return {"prediction": prediction}