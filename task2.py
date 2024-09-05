# a=int(input('enter a number'))
# numbers={0:'zero',1:'one ',2:'two ',3:'three'}
# s=''
# while a>0:
#     d=a%10
#     s=numbers[d]+s
#     a//=10

l=[{'name':'a','age':20,'lang':['mala','eng']}]
s=input("enter new language:")
l[0]['lang'].append(s)
print(l)
