# l=[10,11,2,55,80]
# for i in l:
#     print(i)
    
# l=[10,11,2,55,80]
# if 11 in l:
#     print("yes")
# else:
#     print("no")
"""
yes
"""

# l=[10,22,55,88,21]
# print(l[2])
# l[2]="ibin"
# print(l)
"""
[10, 22, 'ibin', 88, 21]
"""

# l=[10,2,'anu',69,88]
# l.append("add")
# print(l)
# l.extend(['a','b','c'])
# print(l)
# l.insert(0,"insert")
# print(l)

"""
[10, 2, 'anu', 69, 88, 'add']
[10, 2, 'anu', 69, 88, 'add', 'a', 'b', 'c']
['insert', 10, 2, 'anu', 69, 88, 'add', 'a', 'b', 'c']
"""

# l=[10,2,'anu',69,88]
# l.pop()
# print(l)
"""
[10, 2, 'anu', 69]
"""
# l.pop(2)
# print(l)

"""
[10, 2, 69]
"""
# l.remove(69)
# print(l)
"""
[10, 2]
"""
# l=[45,96,42,63,87]
# l.sort()
# print(l)
"""
[42, 45, 63, 87, 96]
"""
# l.reverse()
# print(l)
"""
[96, 87, 63, 45, 42]
"""
# print(l.index(42))
"""
2
"""

# l=[1,5,8,10,11]
# s=0
# for i in l:
#     if i%2==0:
#         print(i)
#         s+=i
# print("sum=",s)

# """
# 8
# 10
# sum= 18
# """


# l=["hello","good", "morning"]
# l.reverse()
# print(l)

# """
# ['morning', 'good', 'hello']
# """


# l=["hello","good", "morning"]
# for i in l:
#     print(i[::-1])

# """
# olleh
# doog
# gninrom
# """

# l=[1,5,3,10,'ibin',55]
# sum=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         sum+=i
# print(sum)
"""
74
"""

# l=[5,8,5,1,2,3,8,5]
# dup=[]
# for i in l:
#     if i not in dup:
#         dup.append(i)
# print(dup)
"""
[5, 8, 1, 2, 3]
"""

# name=[]
# limit=int(input("enter a limit"))
# for i in range(limit):
#     names=input("enter a names:") 
#     name.append(names)
# print(name)

"""
['abi', 'deepa', 'ibin', 'diya', 'seena']
"""

std=[]
limit=int(input("enter a limit"))
for i in range(limit):
    names=input("enter a names:") 
    age=int(input("enter a age:"))
    mark=int(input("enter a mark:")) 
    std.append([names,age,mark])
print(std)