class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email= f" {self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property   #Define the properties
    def printemail(self):  #getter method is used to retrieve the value of a private attribute.
        if self.fname==None or self.lname==None:
            return "Email is not set, Please set it using setter"
        return f" {self.fname}.{self.lname}@gmail.com"
    
    @printemail.setter             #setter can set or modify the value of a private attribute.
    def printemail(self, string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @printemail.deleter
    def printemail(self):
        self.fname=None
        self.lname = None

skillf = Employee("Skill", "F")
print(skillf.email)

print(type(skillf))
print(id(skillf))

o = "this is a string"
print(dir(o))  

import inspect
print(inspect.getmembers(skillf))


A = Employee("Anshu", "Panwar")
B = Employee("Abhishek", "Mishra")

print(A.explain())
print(A.printemail)  #If we want to use directly email then use property decorator.

A.fname = "Sanaya"  #It will not change because constructor already ran on object creation so we use setter
#print(A.email)

print(A.printemail)
A.printemail = "anshu.panwar@gmail.com"
print(A.fname)
print(A.lname)

del A.printemail
print(A.printemail)




