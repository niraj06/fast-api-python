from fastapi import FastAPI

from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/search/10001")
async def default_search():
    return {"default_results": "default search"}


@app.get("/search/{item_id}")
async def search(item_id: int):
    item_list = [10002, 10003, 10004, 10005]
    if item_list.index(item_id):
        return {"result": f"Item found {item_id}"}
    else:
        return {"result": f"Item NOT found {item_id}"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
