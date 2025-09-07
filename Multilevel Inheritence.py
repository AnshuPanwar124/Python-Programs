class Dad:
   basketball = 1

   def isdance(self):
      return f"Yes I dance Parent {self.dance} no of times"

class son(Dad):
   dance =1
   def isdance(self):
      return f"Yes I dance Child {self.dance} no of times"

class Grandson(son):
    dance =6
   
    
darry = Dad()
larry = son()
harry = Grandson()

print(harry.isdance())








