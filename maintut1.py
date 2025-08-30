def abc(string):
    return f"This is a string {string}"

def add(num1, num2):
    return num1+num2+5

print("The name is",__name__) #name is main only in current script.
if __name__ == '__main__' :  #main allows code to be executed only when script is run directly and not when it is imported as a module into another script.

  print(abc("123"))
  c=add(4,3)
  print(c)
