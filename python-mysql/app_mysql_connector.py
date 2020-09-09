import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Admin@123",
  # database="demo"
)

print(connection) 

mycursor = connection.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)