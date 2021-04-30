from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.utilities import haiku_utils

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CreateHaikuRequest(BaseModel):
    starter_words: str = "word word"

class SaveHaikuRequest(BaseModel):
    pseudonym: str
    rating: int


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
async def save_haiku(params: SaveHaikuRequest):
    author_pseudonym = params.pseudonym
    rating = params.rating

    response = {
        "pseudonym": author_pseudonym,
        "rating": rating,
        "status": "success"
    }

    return response
