from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):    #printarea needs to be defined in each subclasses.
        pass
    
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    
    def printarea(self):
        return self.length*self.breadth

    

b = Rectangle()
print(b.printarea())