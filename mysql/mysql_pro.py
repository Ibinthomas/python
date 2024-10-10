import mysql.connector

con =mysql.connector.connect(host='localhost',user='demo',password='demo',port=3307,database='ibindata')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database ibindata")
# cur.execute("create table student (roll int,name text,age int,mark int)")
# cur.execute("insert into student(roll,name,age,mark)values(1,'ibin',20,50)")

# roll=int(input("enter the roll no :"))
# name=input("enter the name :" )
# age=int(input("enter the age :"))
# mark=input("enter the mark :")

# cur.execute('insert into student (roll,name,age,mark)values(%s,%s,%s,%s)',(roll,name,age,mark))

# cur.execute("select * from student")
# data=cur.fetchall()
# for i in data:
#     print(i)

# UPDATE

