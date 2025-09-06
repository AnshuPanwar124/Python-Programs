class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.

    def __init__(self, name, salary, role): #Constructor is used for initialize the object ,called automatically when an object is created from a class.
        self.name = name
        self.salary = salary
        self.role = role
     
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod             # It is bound to the class itself, rather than to an instance of the class.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

class Programmer(Employee):
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}. Language is {self.language}"

    

rohan = Employee("Rohan", 255, "Instructor")
harry = Employee("Harry", 455, "Instructor")

shubham = Programmer("Shubham",555, "Programmer", ["python"])
karan = Programmer("Karan", 500, "Programmer", ["python", "C++"])
harry.change_leaves(34)

#Employee.no_of_leaves = 9
print(harry.no_of_leaves)
print (karan.printprog())
print(karan.printdetails())