from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utilities import haiku_utils

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
    starter_words: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/haiku/create")
async def generate_haiku(params: CreateHaikuRequest):
    generated_haiku = haiku_utils.generate_haiku(params.starter_words)
    return generated_haiku
