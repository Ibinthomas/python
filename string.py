# a="ibin"
# print(a[1])
# print(a[-2])
# print("python","\nfullstack")

#string

# a="possition"
# # print(a[0:5])
# # print(a[2:8])
# # print(a[-2:])

# a=input("enter a string:")
# print(a[::-1])
# print(a==a[::1])

# # string method
# a=input("enter a name")
# # print(a.upper())
# # print(a.lower())
# # print(a.isupper())
# # print(a.islower())
# # print(a.center(10))
# # print(a.count('i'))
# print(a.endswith('n'))

# a=int(input("enter a number"))
# b=int(input("enter second number"))
# if a>=b:
#     print("largest is",a)
# else:
#     print("largest s",b)


# age=int(input("enter age"))
# if age>=18:
#     print("eligible")
# else: 
#     print("not eligible")

# n=int(input("enter a number"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")    

# s=input("enter a string")
# l=input("enter a letter")
# if l in s :
#     print("vissible")
# else:
#     print("not vissible")

# a=int(input("enter a number :"))
# b=int(input("enter a second number :"))
# if a==b:
#     print( "equal")
# elif a>b:
#     print(a)
# else:
#     print(b)


# num=int(input("enter a number:"))
# if num==1:
#     print("sunday")
# elif num==2:
#     print("monday")
# elif num==3:
#     print("tuesday")
# elif num==4:
#     print("wednesday")
# elif num==5:
#     print("thursday")
# elif num==6:
#     print("friday")
# elif num==7:
#     print("saterday")

# city=input("enter the city")
# if city=='delhi':
#     print("Red fort")
# elif city=='agra':
#     print("taj mahal")
# elif city=='jaipur':
#     print("jal mahal")

# price=int(input("enter the price"))
# if price>= 10000:
#     tax=price*0.15
#     print("tax is 15%=",tax)
# elif price>= 50000 and price<=100000:
#     tax=price*10.0
#     print("tax is 10%=",tax)
# elif price<=50000:
#     tax=price*0.05
#     print("tax is 5%=",tax)

# unit=int(input("enter the unit"))
# if unit<= 100:
#     print("no charge")
# elif unit<= 200:
#     bill=(unit-100)*5
# else:
#     bill=(unit-200)*10+500
#     print(bill)

a=int(input("enter a 1st number"))
b=int(input("enter second number"))
c=int(input("enter therd number"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
if b>c:
    print(b)
else:
    print(c)
