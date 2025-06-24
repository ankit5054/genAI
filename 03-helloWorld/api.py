# from typing import Union
from ModipersonaAI import chatModi
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/query/{query}")
# def read_item(query: int, q: Union[str, None] = None):
#     return chatModi(q)
    
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return chatModi(q)