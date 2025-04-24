from fastapi import FastAPI, Query
from pydantic import BaseModel
import wikipedia 



app = FastAPI()

class WikiResponce(BaseModel):
    title:str
    content:str


class LangInput(BaseModel):
    lang:str
    query:str


@app.get("/query", response_model=WikiResponce)
def filter(query:str):
    wikipedia.set_lang("ru")
    page = wikipedia.page(query)
    return {"title": page.title,
            "content": page.content}


@app.get("/{path}", response_model=WikiResponce)
def get_content(path:str):
    wikipedia.set_lang("ru")
    page = wikipedia.page(path)
    return {"title":page.title,
            "content":page.content}


@app.post("/query", response_model=WikiResponce)
def filter_lang(lang_data:LangInput):
    wikipedia.set_lang(lang_data.lang)
    page = wikipedia.page(lang_data.query)
    return {"title": page.title,
            "content": page.content}