lib=[{'id':101,'name':'ibin','email':'ibin@123','address':'kannur','mobile_no':8086939872,'password':123,'book':[]}]
book=[{'book_id':100,'book_name':'manjadi','stock':10,'price':50},{'book_id':id,'book Name':'manjadi','stock':10,'price':50,}]

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
    if uname=='main admin' and password=='main admin':
        f=1
    user=''
    for i in lib:
        if i['email']==uname and i['password']==password:
            f=2
            user=i
    return f,user

def add_book():
    if len(book)==0:
        id=100
    else:
        id=book[-1]['book_id']+1
    book_name=input('Enter book name : ')
    stock=int(input('How many stock in there : '))
    price=int(input('Enter the price : '))
    book.append({'book id':id,'book Name':book_name,'stock':stock,'price':price,})

def view_book():
    print('_'*50)
    print("{:<10}{:<15}{:<10}{:<10}".format('book_id','book_name','stock','price'))
    print('_'*50)
    for i in book:
        print("{:<10}{:<15}{:<10}{:<10}".format(i['book_id'],i['book_name'],i['stock'],i['price']))

def update_book():
    id=int(input('enter the book id to be updated: '))
    f=0
    for i in book:
        if i['book_id']==id:
            f=1
            stock=int(input('enter the updated stock: '))
            price=int(input('enter the updated price: '))
            i['stock']=stock
            i['price']=price
            print('updated successfully')
    if f==0:
        print('invalid id!')

def delete_book():
    id=int(input('enter the book id to be deleted: '))
    f=0
    for i in book:
        if i['book_id']==id:
            f=1
            book.remove(i)
            print('delete!!')
    if f==0:
        print('invalid id!!!')

def display_users():
    print('_'*75)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}".format('id','Name','Email id','Address','mobile No',))
    print('_'*75)
    for i in lib:
        print("{:<10}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email_id'],i['address'],i['mobile_no'],))  

def view_profile(user):
    print('_'*75)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}".format('id','name','email','address','mobile_no',))
    print('_'*75)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}".format(user['id'],user['name'],user['email'],user['address'],user['mobile_no'],)) 


def take_book(user):
    id=int(input('enter the book id: '))
    f=0
    for i in book:
        if i['id']==id:
            f=1
            if i['stock']>0:
                user['books'].append(i['id'])
                i['stock']-=1
            else:
                print('out of stock!!!')
    print(user)
    if f==0:
        print('iinvalid id!!!')

def return_book(user):
    id=int(input('enter the book id: '))
    f=0
    for i in book:
        if i['b_id']==id:
            f=1
            user['books'].remove(i['b_id'])
            i['stock']+=1

while True:
    print('''
    1.ragister
    2.admin login
    3.exit 
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
                    6.exit
                ''')
                
                sub_choice=int(input('Enter the choice :'))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:
                    update_book()
                elif sub_choice==4:
                    delete_book()
                elif sub_choice==5:
                    display_users()
                elif sub_choice==6:
                    break
        elif f==2:
            while True:
                print("""
                    1.View profile
                    2.View book
                    3.Select book
                    4.Return book
                    5.Book in hand
                    6.Exit
                    
                """)
                user_choice=int(input('Enter the choice :'))
                if user_choice==1:
                    view_profile(user)
                elif user_choice==2:
                    view_book()
                elif user_choice==3:
                    take_book(user)
                elif user_choice==4:
                    return_book(user)
                elif user_choice==6:
                    break
                
        else:
            print("invalid user name or password!")
    elif choice==3:
        break    