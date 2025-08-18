inp1 = input("operator")
inp2 = input("First number")
inp3 = input("second number")

new_input = inp2+inp1+inp3

if new_input == "45*3":
    print(555)

elif new_input == "56+9":
    print(77)

elif new_input =="56/6":
    print(4)

elif inp1 == "*":
    print(int(inp2)*int(inp3))

elif inp1 == "+":
    print(int(inp2)+int(inp3))

elif inp1 == "-":
    print(int(inp2)-int(inp3))
    
elif inp1 == "/":
    print(int(inp2)/int(inp3))

