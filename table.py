#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="anjali"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE form (ROLLNO VARCHAR(25), FIRSTNAME VARCHAR(50), LASTNAME VARCHAR(50), DOB VARCHAR(15), EMAILID VARCHAR(50), PASSWORD VARCHAR(50), MOBILENO VARCHAR(10), GENDER VARCHAR(10), ADDRESS VARCHAR(150), COURSESAPPLIEDFOR VARCHAR(10), SEAT VARCHAR(10), BLOODGROUP VARCHAR(10))")
mydb.commit()
print("table created successfully")
mydb.close()
