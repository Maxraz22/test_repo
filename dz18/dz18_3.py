import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9450Rm85",
    database="my_first_db"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

mycursor.close()
mydb.close()