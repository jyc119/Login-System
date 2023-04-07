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

def findTokenLogin(result:str):
    res = ""
    res += result
    for n in table:
        if n[2] == True:
            res += " "+n[0]+","+n[1]
    return res


@app.post("/check-login/")
async def check_login(logindata: LoginDetails):
    username = logindata.username
    password = logindata.password
    token = logindata.token

    if (username,password,False) in table or (username,password,True) in table:
        if token=="yes":
            for i in range(3):
                if table[i] == (username, password, False) or \
                    table[i] == (username,password, True):
                    table[i] = (username,password,1)
        return findTokenLogin("Valid")
    return findTokenLogin("Invalid")

@app.post("/get-usernames/")
async def get_username():
    return "table"

