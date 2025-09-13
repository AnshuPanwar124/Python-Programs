"""
Iterable -- __iter__() or __getitem__() eg : string
Iterator -- __next__()
Iteration -- 

"""
def gen(n):     #Generator returns an iterator object. It use yield to produce a series of results over time.
    for i in range(n):
        yield i 

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

h = "harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


#for c in h:
 #   print(c)

#for i  in range(78):
 #   print(i)