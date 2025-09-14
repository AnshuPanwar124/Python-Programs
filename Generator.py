"""
Iterable -- __iter__() or __getitem__() eg : string --you can create an iterator from an iterable using iter() function.
Iterator -- __next__()  -- It is used to iterate over an iterable.
Iteration -- It is the process of repeatedly executing a block of code for each item in a sequence. eg:for loop, while loop and list comprehension.

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