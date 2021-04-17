from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/haiku/create")
async def generate_haiku(starter_words: str):
    w1, w2 = starter_words.split(",")

    response_body = {
        "starter_words": [w1, w2],
        "haiku": f"{w1.capitalize()} {w2} is all you need in life.",
        "model_version": ""
    }
    return response_body
