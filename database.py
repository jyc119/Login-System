import sqlite3

# List of login infos 
login_list = [
    ("jp201", "fixer"),
    ("jc19", "colon"),
    ("lf12", "tiger")
] 

# Creates the table and inserts the login details
def createTable():
    connection = sqlite3.connect("logins.db")
    cursor = connection.cursor()
    cursor.execute("create table login(user, password)")
    cursor.executemany("insert into login values (?,?)", login_list)
    list = []

    for row in cursor.execute("select * from login"):
        list.append(row)

    connection.close()
    return list