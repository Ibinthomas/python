Carz=[]
while True:
    print('''
        1.Add customer
        2.view
        3.Search
        4.Update
        5.Delete
        6.Exit''')
    choice=int(input("enter the choice:"))
    if choice==1:
        name=input("enter the Owner name:")
        car_no=input("enter the number:")
        mob_no = int(input("Enter Mobile Number: "))
        Address=input("enter the address")
        Carz.append([name,car_no,mob_no,Address,])
        print(Carz)

