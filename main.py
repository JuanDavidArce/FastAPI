# Python
from typing import Optional
from enum import Enum


# Pydantic
from pydantic import BaseModel
from pydantic import Field


# FastAPI
from fastapi import Query,Body,Path
from fastapi import FastAPI

app = FastAPI()


# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black",
    blonde = "blonde"
    red = "red"


class Person(BaseModel):
    first_name:str = Field(
        ...,
        min_length=1,
        max_length=50,
        )
    last_name:str= Field(
        ...,
        min_length=1,
        max_length=50,
        )
    age :int= Field(
        ...,
        gt=0,
        le=115,
    )
    hair_color:Optional[HairColor]=Field(default=None)
    is_married: Optional[bool]= Field(default=None)


class Location(BaseModel):
    city:str
    state: str
    country : str


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
    name:Optional[str]=Query(
        None,min_length=1,
        max_length=50,
        regex="^([A-Z][a-z]+)([\s][A-Z][a-z]+)([\s][A-Z][a-z]+)?([\s][A-Z][a-z]+)?$",
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age:Optional[str]=Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
        )
):
    return {name:age}


# Validations : Path Parameters


@app.get("/person/detail/{person_id}")
def show_person(
    person_id:int= Path(
        ...,
        gt=0,
        )
):
    return {person_id:"It exists"}

# Validations : Request Body


@app.put("/person/{person_id}")
def update_person(
    person_id:int =Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0),
        person:Person =Body(...),
        location: Location = Body(...)

):
    restults = person.dict()
    restults.update(location.dict())
    return restults