import mysql.connector

conn = mysql.connector.connect(username='root', password='Krishnamkmk4422@',host='localhost',database='krish',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()