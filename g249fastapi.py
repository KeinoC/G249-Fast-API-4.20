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


@app.get("/users/{user_id}")
def get_user(user_id: int = Path(None, description="The ID of the item you'd like to view")): ## constraints via path, None is the default value
    return user[user_id]

# Query paramet