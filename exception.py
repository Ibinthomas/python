# a='welcome'
# b=10
# try:
#     print(a+b)
# except:
#     pass
# else:
#     print('error is sxcept not working')
# finally:
#     print('allwase print')



l=[1,2,3,'s',4,5]
s=0
for i in l:
    if type(i)==int or type(i)==float:
        s+=i

# for i in l:
#     try:
#         s+=i
#     except:
#         pass
print(s)
