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
    token: str
    
class LoginDetailsToken(BaseModel):
    username: str
    password: str
    token: bool

inventory = {}
table = database.createTable()

@app.post("/check-login/")
async def check_login(logindata: LoginDetails):
    username = logindata.username
    password = logindata.password
    token = logindata.token

    #table[0] = (username,password,True)
    # for i in range(3):
    #     print(i)
    #     if table[i] == (username, password, False) or \
    #         table[i] == (username,password, True):
    #         return i
    # return -1

    if token=="yes":
        for i in range(3):
            if table[i] == (username, password, False) or \
                table[i] == (username,password, True):
                table[i] = (username,password,1)


    if (username,password) in table:
        return table
    return table
    # if logindata is False:
    #     return "valid"
    # return "invalid"

@app.post("/get-usernames/")
async def get_username():
    return "table"

