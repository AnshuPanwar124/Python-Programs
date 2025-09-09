class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.

    def __init__(self, name, salary, role): #Dunder method always start from underscore and ends with underscore (__)
        self.salary = salary
        self.role = role
        self.name = name
     
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod             # It is bound to the class itself, rather than to an instance of the class.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves
    
    def __add__(self, other):
        return self.salary + other.salary
    
    def __truediv__(self, other):
        return self.salary / other.salary
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary} ,'{self.role}')"
    
    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"



emp1 = Employee("Harry", 66, "Programmer")
#emp2 = Employee("Rohan", 3, "Cleaner")
#print(emp1+emp2)
#print(emp1/emp2)

print(emp1)   #It will firstly run __str__ method .
print(repr(emp1))  #if __str__ will not present then It will run only __repr__