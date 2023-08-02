from typing import Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
fake_items_db = [{
    "name": 'OP', },
    {"name": 'Sun'},
    {"name": 'Run'}
]


class Info(BaseModel):
    name: str
    age: int
    description: Union[str, None] = None


@app.get('/')
async def root():
    return {'message': 'Hello, my friend'}


@app.get('/items/{item_id}')
async def show_item(item_id: int):
    return {"item_id": item_id}


# query параметр, запрос имеет вид: "http://127.0.0.1:8000/items1/&skip=0&limit=10"
@app.get('/items1/')
async def read_item(skip: int = 0, limit: Optional[int] = 10):
    return fake_items_db[skip: skip + limit]


@app.post('/info/', status_code=201)
async def input_information(item: Info):
    return item
