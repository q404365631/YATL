from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import run

app = FastAPI()
users = dict()


class User(BaseModel):
    id: int
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    users[user.id] = {"name": user.name, "info": {"email": user.email}}
    return {"message": "User created"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
