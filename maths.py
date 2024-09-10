def num():
    a=int(input("enter the number"))
    b=int(input("enter the second number"))
    return a,b
def add():
    a,b=num()
    print("sum=",a+b)
def sub():
    a,b=num()
    print("sub=",a-b)
def mult():
    a,b=num()
    print("mult=",a*b)
def div():
    a,b=num()
    print("div=",a/b)
def mode():
    a,b=num()
    print("mod=",a%b)
while True:
    print('''
        1.Add
        2.sub
        3.mult
        4.div
        5.mode
        6.Exit''')

    choice=int(input("enter the choice"))

    if choice==1:
         add()
    elif choice==2:
         sub()
    elif choice==3:
        mult()
    elif choice==4:
        div()
    elif choice==5:
        mode()
    elif choice == 6:
            print("Existing ....!")
    else:
            print("Invalid Choice.")


