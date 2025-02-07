import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='yes',
    database='information_technology'
)
mycursor=mydb.cursor()
#mycursor.execute('create database information_technology')
#mycursor.execute('show databases')
#fetch the databse
#for db in mycursor:
    #print(db)
#mycursor.execute('create table IF NOT EXISTS computer_sci(id int AUTO_INCREMENT PRIMARY KEY,name varchar(400),subject varchar(200),techer_name varchar(400))')
mycursor.execute('SHOW TABLES')
for db in mycursor:
    print(db)
mycursor.close()
mydb.close()