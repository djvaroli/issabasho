from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


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
    w1, w2 = params.starter_words.split(" ")
    response_body = {
        "starter_words": [w1, w2],
        "haiku": f"{w1.capitalize()} {w2} is all you need in life.",
        "model_version": ""
    }
    return response_body
