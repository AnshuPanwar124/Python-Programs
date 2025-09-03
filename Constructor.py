class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.

    def __init__(self, name, salary, role): #Constructor is used for initialize the object ,called automatically when an object is created from a class.
        self.name = name
        self.salary = salary
        self.role = role
     
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry", 455, "Instructor")
print(harry.salary)
'''Rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

Rohan.name = "Rohan"
Rohan.salary = 4554
Rohan.role = "Student"

print(Rohan.printdetails())'''