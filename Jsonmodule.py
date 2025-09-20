import json

'''JSON  (JavaScript Object Notation) is a file that is mainly used to store and transfer data mostly between a server and a web application'''

data = '{"var1":"harry", "var2":56}'
#print(data["var1"])  #we cannot get value without json parsing.

parsed = json.loads(data) #The loads() method is used to parse JSON strings in Python.
print(parsed["var1"])

data2 = {

    "channel name" : "geeks 123",
    "cars" : ["bmw","audi","abc"],
    "fridge" :('roti', 540),
    "isbad" : False
    
    }

jscomp = json.dumps(data2)  #makes compatible with javascript, dump() and dumps() method of json module can be used to convert from Python object to JSON.
print(jscomp)

# Python program to convert JSON to Dict


import json

# JSON string
employee ='{"name": "Nitin", "department":"Finance",\
"company":"GFG"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print("Data after conversion")
print(employee_dict)
print(employee_dict['department'])

print("\nType of data")
print(type(employee_dict))








