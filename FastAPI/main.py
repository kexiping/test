from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    letnet = 'lenet'


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return{"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "letnet":
        return{"model_name": model_name, "message": "LeCNN all the images"}
    
    return{"model_name": model_name, "message": "Have some residuals"}


