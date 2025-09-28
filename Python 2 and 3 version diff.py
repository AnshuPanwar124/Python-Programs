'''
In Python 2.x: dividing two integers performs floor division (discards decimals).
In Python 3.x: dividing two integers performs true division (keeps decimals). 

In Python 2.x: print is a statement (no brackets needed).
In Python 3.x: print is a function, so parentheses are required.

Python 2.x: Strings are ASCII by default, unicode must be defined separately.
Python 3.x: Strings are Unicode by default.

Python 2.x:

range() returns a list.
xrange() returns a generator (saves memory).
Python 3.x:

xrange() is removed.
range() behaves like Python 2’s xrange.

Python 2.x: Uses a comma to bind the exception.
Python 3.x: Uses as keyword (comma syntax no longer works).

__future__ module allows Python 2 code to adopt Python 3 features early, making migration easier.


'''

# Python 2 print 7 / 5             
#print -7 / 5            

print(7 / 5)           
print(-7 / 5)

# Python 2.x
#print 'Hello, Geeks'        # print is a statement
#print('This works too')     # works because it's treated like a function call

# Python 3.x
print('Hello, Geeks')       # print is a function (this is the only correct way)

print(type('default string'))
print(type(b'string with b'))

# Python 2.x
for x in xrange(1, 5):
    print(x),

for x in range(1, 5):
    print(x)

# Python 2.x
try:
    x = not_defined
except NameError, err:
    print err, 'Error Caused'

from __future__ import print_function

print('GeeksforGeeks')





