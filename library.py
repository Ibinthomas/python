lib=[]
book=[]

def reg():
    email=input('Enter the email :')
    f=0
    for i in lib:
        if i['email']==email:
            f1=1
            print("Allready existing email id!!")
            reg()


    if len(lib)==0:
        id=101
    else:
        id=lib[-1]['id']+1
    name=input('Enter your name : ')
    address=input('Enter your address : ')
    mob=int(input('Eneter your mobile number : '))
    password=input('Create a password : ')
    lib.append({'id':id,'name':name,'email':email,'address':address,'mobile_no':mob,'password':password})
    print('registration successfull')

def login():
    uname=input("ente your user name :")
    password=input("enter the password :")
    f=0
    if uname=='admin' and password=='admin':
        f=1
    user=''
    for i in lib:
        if i['email']==uname and i['password']==password:
            f=2
            user=i
    return f,user
def add():
    if (book)==0:
        id=100
    else:
        id=book[-1]['book_id']+1
    book_name=input('Enter your name : ')
    stock=int(input('Eneter the stock : '))
    price=int(input('Create a password : '))
    book.append({'book_id':id,'book_name':book_name,'stock':stock,'price':price,})
    


while True:
    print('''
    1.admin login
    2.exit 
''')
    choice=int(input("Enter the choice :"))
    if choice==1:
        reg()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.Add book
                2.View booK
                3.Update book
                4.Delete book
                5.View user 
            ''')
                
                sub_choice=int(input('Enter the choice :'))
        elif f==2:
            print('user login')
    else:
        print("invalid user name or password!")
    