from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Path parameters

users = {
    1: {"name": "John Doe", "age": 30},
}

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def index():
    return {"hello": "from home"}

@app.get("/users/{user_id}", response_model=User)  # Define response model for /users/{user_id} endpoint
def get_user(user_id: int):
    return users.get(user_id)  # Fix variable name typo here

# Query parameters
