class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.
    pass

harry = Employee()
Rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

Rohan.name = "Rohan"
Rohan.salary = 4554
Rohan.role = "Student"
print(Rohan.name)
print(harry.no_of_leaves)

# Employee.no_of_leaves =  we can change class variable with the help of class name only.
Rohan.no_of_leaves = 9   #It will create new instance variable -- Object's property

print(Rohan.__dict__)
print(Employee.no_of_leaves)

