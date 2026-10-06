import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="change_password",
    database="flaskdb"
)
cursor = mydb.cursor()