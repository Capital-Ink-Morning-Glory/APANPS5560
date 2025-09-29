import spacy
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


class QueryWord(BaseModel):
    word: str  # Define the format of input data

app = FastAPI()

# API router
@app.post("/get_embedding")
def get_embedding(query: QueryWord):
    nlp = spacy.load("en_core_web_lg")
    return {"word": query.word, "embedding": nlp(QueryWord)}