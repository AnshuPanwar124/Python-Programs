import pickle 

''' 
Python pickle module is used for serializing and de-serializing a Python object structure.
Pickling is a way to convert a Python object (list, dictionary, etc.) into a character/byte stream. 
dumps() converts a Python object into a byte string stored in memory. It’s useful when you want to serialize data temporarily, for example, to send over a network or store in a database, without saving it to a file.
loads() takes a byte string that represents a serialized Python object and converts it back into the original object in memory. Use this when you have serialized data in memory and want to recover the original Python structure.
load() reads serialized data from a binary file and reconstructs the original Python object in memory. It is used to load data previously saved using the dump() method.





'''

#Pickling a python object

#cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
#file = "mycar.pkl"
#fileobj = open(file, 'wb')
#pickle.dump(cars, fileobj)
#fileobj.close()

file = "mycar.pkl"  #Unpickling a python object 
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)







