from fastapi import FastAPI, Path

app = FastAPI()



# Path parameters
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(None, description="The ID of the item you'd like to view")): ## constraints via path, None is the default value
    return user[user_id]

# Query paramet