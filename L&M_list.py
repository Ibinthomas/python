# l=[1,2,3,4,5,6,]
# a=filter(lambda x:x%2==0,l)
# print(list(a))
# print(list(filter(lambda x:x%2==0,l)))

# a=['one','two','three','four'] 


# def fun(x):
#     return 't' in x
# print(list(filter(fun,a)))

#MAP
l=[1,2,3,4,5,6,]
#print(list(map(lamda x:x**3,1)))
def fun(x):
    return x**3
print(list(map(fun,l)))

