import sqlite3

# List of login infos 
login_list = [
    ("jc19", "colon", False),
    ("jp201", "fixer", False),
    ("lf12", "tiger", False)
] 

# Creates the table and inserts the login details
def createTable():
    connection = sqlite3.connect("logins.db")
    cursor = connection.cursor()
    cursor.execute("create table login(user, password, token)")
    cursor.executemany("insert into login values (?,?,?)", login_list)
    list = []

    for row in cursor.execute("select * from login"):
        list.append(row)

    connection.close()
    return list