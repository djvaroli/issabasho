import time

from pydantic import BaseModel


class CreateHaikuRequest(BaseModel):
    starter_words: str = "word word"


class SaveHaikuRequest(BaseModel):
    pseudonym: str
    rating: int
    haiku_text: str
    timestamp: int = time.time()
