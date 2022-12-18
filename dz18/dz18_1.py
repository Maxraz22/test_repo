import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9450Rm85",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db")

mycursor.close()
mydb.close()