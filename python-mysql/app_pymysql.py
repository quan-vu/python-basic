import pymysql.cursors  
 
# Connect to database.
connection = pymysql.connect(host='localhost',
                             user='admin',
                             password='Admin@123',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

 
print ("connect successful!!")
