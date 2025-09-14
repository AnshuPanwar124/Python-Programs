#ls = []
#for i in range(100):
 #   if i%3==0:
  #      ls.append(i)

ls = [i for i in range(100) if i%3==0]  #List Comprehension
print(ls)

#dict1 = {i:f"item {i}" for i in range(1001) if i%100==0}   #Dictionary Comprehension
dict1 = {i:f"item {i}" for i in range(5)}
dict2 = {value:key for key,value in dict1.items()}

print(dict1,"\n", dict2)

dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2","dress1", "dress2","dress1", "dress2",]}
print(type(dresses))

evens = (i for i in range(100) if i%2==0) #Generator Comprehension
print(type(evens))
print(evens.__next__())   #Generator is a iterator which can only be iterate once.
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

for item in evens:
    print(item)