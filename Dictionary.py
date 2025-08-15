#Dictionary is a key value pairs, value can be list,tuple or dictionary and key is immutable.
d1={}
print(type(d1))
d2={"Harry":"Burger", "Rohan":"Fish", "SkillF":"Roti", "Shubham":{"B":"maggie","L":"roti","D":"Chicken"}}
print(d2)
print(d2["Harry"])
print(d2["Shubham"])
print(d2["Shubham"]["B"])

d2["Ankit"]="Junk Food"
print(d2)
d2[420]="Kebabs" # key can be int as well
print(d2)

del d2[420]
print(d2)

d3=d2   #Points same reference for both d2 and d3
del d3["Harry"]
print(d2)

d3=d2.copy()  #creates a separate copy...
del d3["Rohan"]
print(d2)
print(d3)
print(d2)

print(d2.keys())
print(d2.items())

print(d2.update({"Anshu":"Beautiful girl"}))
print(d2)

print(d2.values())
print(d2)




