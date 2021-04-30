from datetime import datetime as dt
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.utilities import haiku_utils, redis_utils
from app.utilities.pydantic_models import *


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Haiku generator welcomes you."}


@app.post("/haiku/create")
async def generate_haiku(params: CreateHaikuRequest):
    generated_haiku = haiku_utils.generate_haiku(params.starter_words)

    response = {
        "haiku": generated_haiku,
        "model_version": 1
    }
    return response


@app.post("/haiku/save")
async def save_haiku(haiku_data: SaveHaikuRequest):
    status = 1

    try:
        redis_utils.store_haiku_rating(haiku_data)
    except Exception as e:
        status = 0

    response = {"status": status}
    return response
