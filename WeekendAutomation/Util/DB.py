import mysql.connector
db = mysql.connector.connect(
host ="localhost",
port=3306,
user= "root",
password= "Password",
database="SATYA")
cursor = db.cursor()
# cursor.execute("IF data is present")
# sql= "create table DATA(Name Varchar(255),Age int)"
# cursor.execute(sql)
# cursor.execute("Select * from test")
# result=cursor.fetchall()
# print(result)
# for row in result:
#     print(row)

cursor.execute("INSERT INTO test VALUES(3,'Ashish',29,'hari@test.com')")
db.commit()
cursor.execute("Select * from test")
result=cursor.fetchall()
print(result)
for row in result:
    print(row)
cursor.close()
db.close()
