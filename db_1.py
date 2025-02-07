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
#mycursor.execute('SHOW TABLES')
sql="INSERT INTO computer_sci (id, name, subject, techer_name) VALUES (%s, %s, %s, %s)"
val = [
    (1, "Alice", "Data Structures", "Dr. Smith"),
    (2, "Bob", "Algorithms", "Dr. Johnson"),
    (3, "Charlie", "Operating Systems", "Dr. Brown"),
    (4, "David", "Database Systems", "Dr. Miller"),
    (5, "Eve", "Computer Networks", "Dr. Wilson"),
    (6, "Frank", "Artificial Intelligence", "Dr. Lee"),
    (7, "Grace", "Cybersecurity", "Dr. Adams"),
    (8, "Henry", "Web Development", "Dr. White"),
    (9, "Ivy", "Cloud Computing", "Dr. Harris"),
    (10, "Jack", "Software Engineering", "Dr. Thompson"),
    (11, "Karen", "Machine Learning", "Dr. Garcia"),
    (12, "Leo", "Deep Learning", "Dr. Martinez"),
    (13, "Mia", "Computer Vision", "Dr. Robinson"),
    (14, "Noah", "Human-Computer Interaction", "Dr. Clark"),
    (15, "Olivia", "Parallel Computing", "Dr. Rodriguez"),
    (16, "Paul", "Blockchain Technology", "Dr. Lewis"),
    (17, "Quinn", "Game Development", "Dr. Walker"),
    (18, "Rachel", "Big Data Analytics", "Dr. Hall"),
    (19, "Sam", "Cloud Security", "Dr. Allen"),
    (20, "Tina", "Mobile Computing", "Dr. Young"),
    (21, "Uma", "Internet of Things", "Dr. King"),
    (22, "Victor", "Embedded Systems", "Dr. Wright"),
    (23, "Wendy", "Quantum Computing", "Dr. Scott"),
    (24, "Xander", "Bioinformatics", "Dr. Green"),
    (25, "Yvonne", "Cryptography", "Dr. Baker"),
    (26, "Zane", "Edge Computing", "Dr. Adams"),
    (27, "Anna", "DevOps", "Dr. Carter"),
    (28, "Ben", "Computer Graphics", "Dr. Rivera"),
    (29, "Clara", "Robotics", "Dr. Perez"),
    (30, "Daniel", "Network Security", "Dr. Lopez"),
    (31, "Elsa", "Programming Languages", "Dr. Hill"),
    (32, "Felix", "Neural Networks", "Dr. Scott"),
    (33, "George", "Computational Biology", "Dr. Evans"),
    (34, "Hannah", "Natural Language Processing", "Dr. Adams"),
    (35, "Ian", "Digital Forensics", "Dr. Collins"),
    (36, "Julia", "Smart Systems", "Dr. Stewart"),
    (37, "Kevin", "Software Testing", "Dr. Turner"),
    (38, "Lara", "Computer Ethics", "Dr. Hughes"),
    (39, "Mike", "Theoretical CS", "Dr. Murphy"),
    (40, "Nancy", "Distributed Systems", "Dr. Foster"),
    (41, "Oscar", "UI/UX Design", "Dr. Richardson"),
    (42, "Penny", "Embedded AI", "Dr. Howard"),
    (43, "Ron", "Cloud Architecture", "Dr. Ramirez"),
    (44, "Sophia", "Software Architecture", "Dr. Cooper"),
    (45, "Tom", "High-Performance Computing", "Dr. Ward"),
    (46, "Ursula", "Computer Simulation", "Dr. Torres"),
    (47, "Victor", "Pervasive Computing", "Dr. Peterson"),
    (48, "Wanda", "Database Administration", "Dr. Gray"),
    (49, "Xena", "Functional Programming", "Dr. Price"),
    (50, "Yusuf", "Game AI", "Dr. Bell")
]

mycursor.executemany(sql,val)
mydb.commit()
#for db in mycursor:
    #print(db)
print(mycursor.rowcount)    
mycursor.close()
mydb.close()