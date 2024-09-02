d={'name': 'ibin',
   'age': '20'}
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

print(d.get('name'))
print(d.values())
print(d.keys())
print(d.items())
d.update({'mark':'100'})
print(d)
"""
dict_values(['ibin', '20'])
dict_keys(['name', 'age'])
dict_items([('name', 'ibin'), ('age', '20')])
{'name': 'ibin', 'age': '20', 'mark': '100'}
"""