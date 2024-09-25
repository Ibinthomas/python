# f=open('python/ibin.txt','x')
# f=open('python/ibin.txt','r')


# f.write('welcome to all')

# print(f.read())
# a=f.read(5)
# f.seek(3)
# b=f.read()
# print(f.tell())
# print(a)
# print('_'*25)
# print(b)


# a=f.readline(5)
# b=f.readline()
# print(a)
# print(b)
# c=f.readlines()
# print(c)


# l=f.readlines()
# f.seek(2)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a)

# f=open('python/ibin.txt','r')

# l=f.readline()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a[::-1])

f=open('python/ibin2.txt','r')
l=f.readline()
f.seek(0)
letter=0
cap=0
word=0
# for i  in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)

for i  in range(len(l)):
    a=f.readline().strip()
    s=a.split(' ')
    for i in s:
        if i!='':
            word+=1
    for i in a:
        if i!=' ':
            if i.isupper():
                cap+=1
    for i in a:
        l= l.strip()
    letter+=1
print(letter)
print('cap',cap)
print('small',letter-cap)
print("total word",word)
print('no of lines',len(l))
