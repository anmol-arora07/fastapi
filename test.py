from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from enum import Enum
from fastapi.websockets import WebSocket,WebSocketDisconnect
import time
import random

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


@app.get("/progress")
async def progress(request: Request):
    return templates.TemplateResponse("progress.html" ,{"request": request})


connected_clients = set()

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)

    try:
        count=0
        while count<10:
            # Continuously send log messages to the client
            log_message =  get_next_log_message()
            await websocket.send_text(log_message)
            count+=1
    except WebSocketDisconnect:
        connected_clients.remove(websocket)



log_messages = [
    "This is an informational log message",
    "This is another log message",
    "An error occurred",
    "Warning: Invalid input detected",
    "Debugging information"
]

def get_next_log_message():
    # Simulate fetching the next log message from a logging system
    # Replace this logic with your actual implementation

    # Randomly select a log message from the list
    log_message = random.choice(log_messages)
    
    # Simulate some processing time
    time.sleep(1)

    return log_message