import sqlite3

release_list = [
    ("jp201", "fixer"),
    ("jc19", "colon"),
    ("lf12", "tiger")
] 

def createTable():
    connection = sqlite3.connect("logins.db")
    cursor = connection.cursor()
    cursor.execute("create table login(user, password)")
    cursor.executemany("insert into login values (?,?)", release_list)
    list = []

    #print database rows
    for row in cursor.execute("select * from login"):
        list.append(row)

    connection.close()
    return list