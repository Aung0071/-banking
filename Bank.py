import mysql.connector

 
connection = mysql.connector.connect(user = 'root', database = 'banking', password = '')

 

cursor = connection.cursor()

 

testQuery = ('SELECT * FROM banks')

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()