import spacy
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

nlp = spacy.load("en_core_web_lg")

app = FastAPI()

templates = Jinja2Templates(directory="templates")  # The directory of the HTML template

@app.get("/", response_class=HTMLResponse)  # Input the query word
async def form_page(request: Request):
    return templates.TemplateResponse("ui.html", {"request": request, "embedding": None})


@app.post("/embed", response_class=HTMLResponse)
async def get_embedding(request: Request, query_word: str=Form(...)):
    word = nlp(query_word)
    return templates.TemplateResponse(
        "ui.html", {"request": request, "word": query_word, "embedding": word.vector.tolist()}
    )