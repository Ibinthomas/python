std=[]
while True:
    print("""""
          1.add student
          2.display student details
          3.update student
          4.delet student
""")
    choice=int(input("enter your choice" ))
    if choice==1:
        names=input("enter a names:") 
        age=int(input("enter a age:"))
        mark=int(input("enter a mark:")) 
        std.append([names,age,mark])
    elif choice==2:
        print('{:<10},{:5},{:<5}'.format('name''age''mark'))
        print()