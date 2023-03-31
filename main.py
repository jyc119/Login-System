from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import database

app = FastAPI()

class LoginDetails(BaseModel):
    username: str
    password: float

inventory = {}
table = database.createTable()

@app.post("/create-login/{user_id}")
def create_login(user_id:int, login:LoginDetails):
    if user_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exist")
    
    inventory[user_id] = login
    return inventory[user_id]


@app.post("/check-login/")
def check_login(logindata: LoginDetails) -> dict:
    username = logindata.username
    password = logindata.password
    if (username,password) in table:
        return {"result": "Correct"}
    return {"result": "Incorrect"}

