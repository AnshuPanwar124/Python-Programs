grocery = ["Harpic", "Vim bar","bindi","lollypop",56]  #Index starts from 0
print(grocery[2])
numbers=[2,7,9,11,3]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[0:5])
numbers.append(71)
print(numbers)
numbers.insert(1,91) #It takes index and numbers need to be added 
print(numbers)
numbers.remove(9)
print(numbers)
numbers.pop() #removes last element from list
print(numbers)

#mutable == can change (list)
#immutable == cannot change (tuple)

tp=(1,2,3)
#tp[1]=8
print(tp)

a=1
b=9
a,b=b,a
print(a,b) # Swapping numbers



