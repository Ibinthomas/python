import sqlite3

con=sqlite3.connect('python/database/demo.db')

try:
    con.execute("create table student(roll_no int,name text,age int,mark real)")
except:
    print("table exist")

# con.execute("insert into student (roll_no,name,age,mark)values(1,'deepak',21,20),(2,'ibin',21,30),(3,'alen',20,21)")
# con.commit()

# n=int(input("enter the limit"))
# print("*"*20)
# for i in range(n):
#     roll=int(input("enter roll no :"))
#     name=input("enter name :")
#     age=int(input("enter thr age :"))
#     mark=float(input("enter the mark :"))

#     con.execute('insert into student(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#     con.commit()

# data=con.execute("select * from student")
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MAEK'))
# print('*' * 60)
# for i in data:
#     # print(i[0])
#     print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    

# USING CONDITION
# n=int(input("enter the  vakue"))

# data=con.execute("select * from student where roll_no=?",(n,))
# print('_' * 60)
# print('{:<10}{:<10}{:<10}{:<10}'.format('ROLL NO','NAME','AGE','MAEK'))
# print('*' * 60)
# for i in data:
#     # print(i[0]) 
#       print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    

 
# updating


# name=input("enter the name :" )
# n_name=input("enter the second name : ")
# con.execute("update student set name=? where name=?",(n_name,name))
# con.commit()

# r=input("enter the deletd student roll no :")
# con.execute("delet from student where roll_no=?",(r,))
# con.commit()

# like

# data=con.execute("select * from student where name like 'a%'")
# for i in data:
#     print(i)


# order by

# data=con.execute("select * from student order by name")
# for i in data:
#     print(i)

# DESCINDING ORDER 

# data=con.execute("select * from student ORDER BY NAME DESC")
# for i in data:
#     print(i) 

# GROUP BY 

# data=con.execute("select * from student group by name")
# for i in data:
#     print(i)

# AGGRIGATE FUNCTION

# MAX
data=con.execute("select name,max(mark) from student group by name")
for i in data:
    print(i)

# MIN
data=con.execute("select name,mix(mark) from student group by name")
for i in data:
    print(i)

# AVG
data=con.execute("select name,avg(mark) from student group by name")
for i in data:
    print(i)