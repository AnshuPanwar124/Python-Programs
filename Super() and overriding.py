class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"  # It will check first B instance var then A instance var then B class var then A class var .

    def __init__(self):
        super().__init__()  #called Parent Class constructor
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"


a = A()
b = B()

print(b.classvar1)
print(b.special)
print(a.classvar1)