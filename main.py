# Python
from typing import Optional


# Pydantic
from pydantic import BaseModel


# FastAPI
from fastapi import Query
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


# Models


class Person(BaseModel):
    first_name:str
    last_name:str
    age :int
    hair_color:Optional[str]=None
    is_married: Optional[bool]=None

@app.get("/")
def home():
    return {"Hello":"world"}

# Request and Response Body
@app.post('/person/new')
def create_person(person:Person=Body(...)):
    return person


# Validations: Query Parameters

@app.get("/person/detail")
def show_person(
    name:Optional[str]=Query(None,min_length=1,max_length=50,regex="^([A-Z][a-z]+)([\s][A-Z][a-z]+)([\s][A-Z][a-z]+)?([\s][A-Z][a-z]+)?$"),
    age:Optional[str]=Query(...)
):
    return {name:age}
