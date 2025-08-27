'''
me = "Harry"
a1 = 3
a = "this is %s %s"%(me,a1)
print(a)

The above code is for string formatting but it is not readible and for large variable.

'''
import math
me = "Harry"
a1 = 3
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)

#Use Fstring for more readability purpose.

a = f"this is {me} {a1} {4*65} {math.cos(65)}"
print(a)

