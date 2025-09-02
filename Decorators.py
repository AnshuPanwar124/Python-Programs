def function1():
    print("Subscribe now")

fun2 = function1
del function1
fun2()

def funcret(num):
    if num==0:
        return print
    if num ==1:
        return sum
a=funcret(1)
print(a)


def executor(func):
    func("this")

executor(print)

def dec1(func1):    #Decorator is used to modify or extend behaviour of functions or methods without changing their actual code,takes function as argument and returns a new function.
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)           same as @doc

who_is_harry()