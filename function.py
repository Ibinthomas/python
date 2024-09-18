# def fun():
#     print("python")
#     print("welcome")
#     print("hellow world")

# fun()
# print("*"*10)
# fun()
# print("*"*10)
# fun()

# def fun1():
#     b=10
#     print('b=',b)

# b=20
# fun1()
# print(b)

# def fun2():
#     global a
#     a=10
#     print(a)
# print("local into globel",a)

# def fun3():
#     return 'welcome',10
# a,b=fun3()
# print(a)
# print(b)

# def fun4():
#     a=1
#     b=2
#     c=3
#     return a,b,c
# a1,b1,c1=fun4()
# print(a1)
# print(b1)
# print(c1)


# Arbitary argument

# def aa(b,*a):
#     print(b,a)

# aa(5,6)
# aa(3,344,555,46,21)

# Arbitary keyword argument

# def aka(**a):
#     print(a)

# aka(name='ibn',age=20,snnme='deepak',seage=21,)    




def numbers():
    a=int(input("Enter a fist no :"))
    b=int(input("Enter a second no :"))
    return a,b
add=lambda a,b:a+b
sub=lambda a,b:a-b
div=lambda a,b:a/b
mult=lambda a,b:a*b
mod=lambda a,b:a%b

while True:
    print('''
        1.addition
        2.subtracton
        3.divition
        4.multi
        5.modulas
        6.exit
       ''')
    choice=int(input("enter the choice :"))
    if choice==1:
        a,b=numbers()
        print(add(a,b))
    elif choice==2:
        a,b=numbers()
        print(sub(a,b))
    elif choice==3:
        a,b=numbers()
        print(div(a,b))
    elif choice==4:
        a,b=numbers()
        print(mult(a,b))
    elif choice==5:
        a,b=numbers()
        print(mod(a,b))
    elif choice==6:
        break
print("invalid choice")

