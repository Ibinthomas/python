std=[]
while True:
    print("""
          1.add student
          2.display student details
          3.update student
          4.delet student
          5.search
          6.break
""")
    choice=int(input("enter your choice :" ))
    if choice==1:
        names=input("enter a names:") 
        age=int(input("enter a age:"))
        mark=int(input("enter a mark:")) 
        std.append([names,age,mark])
    elif choice==2:
        print('{:<10}{:5}{:<5}'.format('name','age','mark'))
        print('*'*20)
        for i in std:
            print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input("enter a name:")
        f=0
        for i in std:
            if i[0]==name:
                mark=int(input("enter new mark"))
                i[2]=mark
                f=1
        if f==0:
            print("name not in list")
    elif choice==4:
        name =input("enter name")
        for i in std:
            if i[0]==name:
                std.remove(i)
                f=1
        if f==0:
            print('name not found in the list')
    elif choice==5:
        name= input("enter a name")
        f=0
        for i in std:
            if i[0]==name:
                print(i)
        if f==0:
            print("std not in list")
    elif choice==6:
        break
    else:
            print("invalid choice")