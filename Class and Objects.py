class Student:
    
   pass

harry = Student()
larry = Student()

harry.name = "harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi","physics"]
print (harry.std, larry.subjects)

print(harry,larry)     # Both are different objects pointing to diff memory location