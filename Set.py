s = set()
print(type(s))

s_from_list = set([1,2,3,4,5])
print(s_from_list)

s.add(1)
s.add(2)   #Set is unique collection of items that is the reason It will not include second 1
s1=s.union({1,2,3})
s2=s.intersection({1,2,3})
print(s,s1)
print(s,s2)

print(s.isdisjoint(s1))





