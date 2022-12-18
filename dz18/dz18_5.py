import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9450Rm85",
    database="my_first_db"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = (1, "John")
mycursor.execute(sql, val)
mydb.commit()
mycursor.close()

mycursor = mydb.cursor()
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = (1, "John", 10000)
mycursor.execute(sql, val)
mydb.commit()
