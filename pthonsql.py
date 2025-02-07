import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="yes",
    database="school_db"
)
mycursor = mydb.cursor()

mycursor.execute('')


mycursor.close()
mydb.close()
