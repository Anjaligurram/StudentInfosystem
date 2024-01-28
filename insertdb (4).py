#!C:\Program Files (x86)\Python38-32/python.exe
print("Content-Type:text/html\n")
import cgi, cgitb
import pymysql
cgitb.enable() 
import sys
form=cgi.FieldStorage()
rn = form.getvalue('ROLLNO')
fn = form.getvalue('FIRSTNAME')
ln = form.getvalue('LASTNAME')
do = form.getvalue('DOB')
em = form.getvalue('EMAILID')
pa = form.getvalue('PASSWORD')
mo = form.getvalue('MOBILENO')
ge = form.getvalue('GENDER')
ad = form.getvalue('ADDRESS')
co = form.getvalue('COURSESAPPLIEDFOR')
se = form.getvalue('SEAT')
bg = form.getvalue('BLOODGROUP')
con=pymysql.connect(user='root',password='',host='localhost',
                                database='anju')
cur=con.cursor()
sql = "INSERT INTO form (ROLLNO,FIRSTNAME,LASTNAME,DOB,EMAILID,PASSWORD,MOBILENO,GENDER,ADDRESS,COURSESAPPLIEDFOR,SEAT,BLOODGROUP) VALUES(%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)"
val = (rn, fn, ln, do, em, pa, mo, ge, ad, co, se, bg)
cur.execute(sql, val)
con.commit()
cur.close()
print("data inserted into table successfully")
