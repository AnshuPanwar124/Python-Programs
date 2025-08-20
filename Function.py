#a = 9
#b = 8
# c = sum((a,b))  Built in function

def function1(a,b):
    print("hello you are in function 1",a+b)

def function2(a,b):
    """ This is a function which will calculate average of two numbers"""
    average = (a+b)/2
    print(average)
    return(average)

v = function2(5,7)
print(v)              #It will print none, will not return any value .
print(function2.__doc__)  # It will show doc of that function

function1(5,7)
