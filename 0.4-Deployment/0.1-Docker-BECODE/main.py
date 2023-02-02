from fastapi import FastAPI

from model.UserRequest import UserRequest
from repository.modelManager import ModelManager

app = FastAPI()

modelManager = ModelManager()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/makePrediction")
async def make_prediction(requestData: UserRequest):
    price = await modelManager.make_prediction(requestData)
    return {"price": price}
