# d={'name': 'ibin',
#    'age': '20'}
# print(d)
# print(d['age'])
# d['name']="abhi"
# print(d)
# d['palce']='kochikode'
# print(d)
"""
{'name': 'ibin', 'age': '20'}
20
{'name': 'abhi', 'age': '20'}
"""
# for i in d:
#     print(i,":",d[i])

# if d['name']=='ibin':
#     print('true')
# else:
#     print("no")

# print(d.get('name'))
# print(d.values())
# print(d.keys())
# print(d.items())
# d.update({'mark':'100'})
# print(d)
"""
dict_values(['ibin', '20'])
dict_keys(['name', 'age'])
dict_items([('name', 'ibin'), ('age', '20')])
{'name': 'ibin', 'age': '20', 'mark': '100'}
"""
# d={}
# l=['name','age','mark','place']
# d=d.fromkeys(l)
# print(d)
"""
{'name': None, 'age': None, 'mark': None, 'place': None}
"""
# d={}
# d.setdefault('name')
# print(d)
"""
{'name': None}
"""

# std=[{'name':'a','age':20},
#      {'name':'b','age':30},
#      {'name':'c','age':25},
#      {'name':'d','age':35}]
# b=[]
# a=[]
# for i in std:
#     if i['age']<30:
#         b.append(i)
#     else:
#         a.append(i)
# print("above in 30")
# print('{:<10}{:<5}'.format('name','age'))
# for i in a:
#    print('{:<10}{:<5}'.format(i['name'],i['age']))
# print("below in 30")
# print('{:<10}{:<5}'.format('name','age'))
# for i in b:
#     print('{:<10}{:<5}'.format(i['name'],i['age']))

num={}
n=int(input("enter a number"))
for i in range(n+1):
   print(i) 
   num[i]=i*i
print(num)
