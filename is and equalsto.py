#== - value equality - Two objects have the same Value
# is - reference equality - Two objects refer to the same object.

a = [7,4,5]
b=a

print(b == a)
print(b is a)  # pointing to same object.

c = a[:]
print(a==c)
print(c is a)