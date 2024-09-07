# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print(s.intersection(s1))
# print("union=",s.union(s1))
# print("isdissjoint=",s.isdisjoint(s1))
# print("issubset",s.issubset(s1))
# print("issuperset=",s.issuperset(s1))
# print("issuperset=",s.symmetric_difference(s1))

s={1,2,3,4,5}
s1={1,2,3,6,7}
s.difference_update(s1)
print(s)
s.intersection_update(s1)
print(s)
s.symmetric_difference_update(s1)
print(s)
