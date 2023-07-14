from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from enum import Enum

templates = Jinja2Templates(directory="template")
app = FastAPI()

@app.get("/")
async def hello(request:Request):

    
    return templates.TemplateResponse("index.html", {"request": request})



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
 

@app.post("/form-data")
async def receive_form_data(form_data: dict):
    # Process the received form data
    print(form_data)
    return {"message": "Form data received"}
