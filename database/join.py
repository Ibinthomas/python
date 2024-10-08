import sqlite3

con=sqlite3.connect('python/database/join.db')

try:
    con.execute("create table student(roll_no int,name text,age int)")
except:
    print("table exist")

try:
    con.execute("create table mark(roll_no int,subject text,mark int)")
except:
    print("table exist")

# con.execute("insert into student(roll_no,name,age)values(1,'ibin',20),(2,'deepak',21),(3,'ajin',23)")
# con.commit()
# con.execute("insert into mark(roll_no,subject,mark)values(1,'cyber',100),(2,'devops',120),(3,'python',23)")
# con.commit()


# data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from student join mark on student.roll_no=mark.roll_no")
# for i in data:
#     print(i)


# data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from mark left join student on student.roll_no=mark.roll_no")
# for i in data:
#     print(i)

# cross join

data=con.execute("select student.roll_no,student.name,student.age,mark.subject,mark.mark from student cross join mark")
for i in data:
    print(i)