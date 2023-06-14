from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def hello():
    return "Hello World"


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model (model_name: ModelName):
    if model_name=="alexnet":
        return {"model name": model_name.value}
    
