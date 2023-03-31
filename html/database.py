import sqlite3

connection = sqlite3.connect("logins.db")
cursor = connection.cursor()

cursor.execute("create table login(user, password)")

release_list = [
    ("jp201", "fixer"),
    ("jc19", "colon"),
    ("lf12", "tiger")
] 

cursor.executemany("insert into login values (?,?)", release_list)

#print database rows
for row in cursor.execute("select * from login"):
    print(row)

connection.close()