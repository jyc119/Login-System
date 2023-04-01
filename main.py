from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import database

app = FastAPI()

# added this to app for cross origin resource sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
The class used to hold in my login details. 
Fields are usernames and password
"""
class LoginDetails(BaseModel):
    username: str
    password: str

inventory = {}
table = database.createTable()

@app.post("/check-login/")
async def check_login(logindata: LoginDetails):
    username = logindata.username
    password = logindata.password

    if (username,password) in table:
        return table
    return table

@app.post("/get-usernames/")
async def get_username():
    return "table"

