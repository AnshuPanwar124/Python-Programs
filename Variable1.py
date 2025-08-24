l=10  #Global

def function1(n):
   # l=5 #local
    m=8 #local
    #l=l+45   #we cannot modify Global var inside local that's why we require global keyword.
    global l
    l=1
    l=l+45

    print(l,m)
    print(n, "I have printed")

print(l)

function1("This is me")
#print(m)  #Local variable cannot be accessed outside the function.

def harry():
    x=20
    def rohan():
        global x  #Global search for global var not local that is the reason It will not change 88 from 20.
        x=88   #It will create global variable of 88
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)