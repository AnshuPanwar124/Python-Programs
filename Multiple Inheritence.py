class Employee:
    no_of_leaves = 8   #Class variable is class Property, It is shared by all instances of that class.
    var = 8

    def __init__(self, name, salary, role): #Constructor is used for initialize the object ,called automatically when an object is created from a class.
        self.name = name
        self.salary = salary
        self.role = role
     
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod             # It is bound to the class itself, rather than to an instance of the class.
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

class Player:
    no_of_games = 4
    var = 9
    def __init__(self,name,game):
        self.name=name
        self.game=game

class CoolProgrammer(Employee,Player):  #This arg order is important and should be in order and if same var/function declared in both the class present in arg then It will take first class var/func defined in the arg.
    language = "C++"
    var = 10

    def printlanguage(self):
        print(self.language)

    

rohan = Employee("Rohan", 255, "Instructor")
harry = Employee("Harry", 455, "Instructor")

Shubham = Player("Shubham",["Cricket"])
karan = CoolProgrammer("karan", 9999, "CoolProgrammer")
print(karan.printdetails())
karan.printlanguage()
print(karan.var)

harry.change_leaves(34)

#Employee.no_of_leaves = 9
print(harry.no_of_leaves)

