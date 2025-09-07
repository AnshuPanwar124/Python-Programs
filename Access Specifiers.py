class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.
    _protect = 9    #Protected variable can be accessed within the class and its subclasses.
    __private = 10  #Private variable can be accessed within the class.

    def __init__(self, name, salary, role): #Constructor is used for initialize the object ,called automatically when an object is created from a class.
        self.name = name
        self.salary = salary
        self.role = role
     
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod             # It is bound to the class itself, rather than to an instance of the class.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

emp = Employee ("Harry", 500 , "Programmer")
print(emp._protect)
print(emp._Employee__private)

