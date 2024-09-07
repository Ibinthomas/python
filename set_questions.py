s=set()
l=int(input("enter a limit php:"))
for i in range(l):
    name=input("enter a names:")
    s.add(name)
print(s)

python=set()
l=int(input("enter the limit python:"))
for i in range(l):
    name=input("enter the name:")
    python.add(name)
print(python)

java=set()
l=int(input("enter the limit java:"))
for i in range(l):
    name=input("enter the name:")
    java.add(name)
print(java)

# n=s.intersection(python)
# n.intersection(java)
# print("names:",n)

a=python.difference(s)
a.difference(java)
print(a)


