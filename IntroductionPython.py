from functools import singledispatch

@singledispatch
def fun(arg):
    print("Default implementation, arg:", arg)

@fun.register(int)
def _(arg):
    print("Integer implementation, arg:", arg)

@fun.register(str)
def _(arg):
    print("String implementation, arg:", arg)

fun(10)      # Calls int version
fun("abc")   # Calls str version
fun([1,2,3]) # Calls default version