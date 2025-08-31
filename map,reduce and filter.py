numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))  # It is used to apply a specific function to each element of an iterable and returns a map object.

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

numbers[2]=numbers[2]+1
print(numbers[2])

num = [2,3,5,6,76,3,3,2]
square = print(list(map(lambda x : x*x, num)))

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
for i in range(6):
    val = list(map(lambda x:x(i), func))
    print(val)



list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = filter(is_greater_5, list_1)  #It is used to extract elements from an iterable (list, tuple or set) that satisfy a given condition.
print(list(gr_than_5))


from functools import reduce

list1 = [1,2,3,4,7]
num =reduce(lambda x,y:x+y, list1)  #It applies a given function cumulatively to all items in an iterable, reducing it to a single final value.
print(num)
