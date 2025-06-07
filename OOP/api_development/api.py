from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Person(BaseModel):
    name: str
    age: int


class PersonResponse(BaseModel):
    message: str

@app.post("/create_person")
async def create_person(person: Person):
    return {"message": f"Person {person.name} created with age {person.age}"}

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.post("/create_person/", response_model=PersonResponse)
async def create_person(person: Person):
    return {"message": f"Person {person.name} created with age {person.age}"}
