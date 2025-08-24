def fac_recursive(n):

    if n==1:
        return 1
    
    else : 
        return n * fac_recursive(n-1)
    
number = int(input("Enter the number to know it's factorial\n"))
print("Factorial using Recursive Method",fac_recursive(number))


#Factorial using Iterative method..

def fac_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)   
    return fac
    
number = int(input("Enter the number to know it's factorial\n"))
print("Factorial using Iterative Method",fac_iterative(number))

#Fibonacci series = 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n==1:    #It means first index
        return 0
    elif n==2:   # It means second index
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
number=int(input("Enter a number to know it's fibonacci"))
print(fibonacci(number))


    

