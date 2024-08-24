# i=int(input("starting number"))
# l=int(input("ending number"))
# while i<=l:
#     print(i)
#     i+=1

# factorial
# a=int(input("enter a number:" ))
# i=1
# f=1
# while i<=a:
#     f*=i
#     i+=1
# print(f)

# revers of a number
# n=int(input("enter the numbers : "))
# i=0
# rev=0
# while n>0:
#     d=n%10
#     print(d)
#     n//=10

# n=int(input("enter the numbers : "))
# i=0
# r=0
# while n>0:
#     d=n%10
#     r=r*10+d
#     n//=10
# print("reverse=",r)

# n=int(input("enter the numbers : "))
# i=0
# r=0
# while n>0:
#     d=n%10
#     r=r+d
#     n//=10
# print("reverse=",r)

# a=input("enter a string  :")
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i+=1

# for i  in range(11):
#     print(i)

# for i in range(2,11):
#     print(i)

# for i in range(3,100,5):
#     print(i)

# a=int(input("enter startig number"))
# e=int(input("enter end number"))
# sum=0
# for i in range(a,e+1):
#     print(i)
#     sum+=i
# print("number of sum=",sum)

#  sum or even numbers

# s=int(input("enter thr starting number"))
# e=int(input("enter the ending number"))
# sum=0
# for i in range(s,e+1):
#     if i%2==0:
#         print(i)
#     sum+=i
# print("sum of even number",sum)

# s=input("enter a number")
# r=''
# for i in s:
#     r=i+r
# print("revrs a string:",r)

# for i in range(4):
#     print("i=",i)
#     for j in range(3):
#         print("\tj=",j)

# for i in range(5):
#     for j in range(5):
#         print(j,end="\t")
#         print()

# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#     print()

###
    # 000
    # 111
    # 222
###

# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#         i+=1
#     print()
# 0 1 2 
# 1 2 3 
# 2 3 4 

# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=1
#     print()
# #0 1 2 
# #4 5 6 
# #7 8 9 

for i in range(4):
    if i%2==0:
        for j in range(3):
            print(j,end="\t")
    else:
       for j in range(3):
        print(2-j,end="\t")
    print()