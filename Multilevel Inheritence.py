class Dad:
   basketball = 1

class son(Dad):
   dance =1
   def isdance(self):
      return f"Yes I dance {self.dance} no of times"

class Grandson(son):
    dance =6
    def isdance(self):
      return f"Yes I dance very awesomly {self.dance} no of times"
    
darry = Dad()
larry = son()
harry = Grandson()

print(harry.isdance())








