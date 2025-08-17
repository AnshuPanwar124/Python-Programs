i=0

while(True):
    if i+1<5:
      i=i+1
      continue #skip the rest of the current iteration of a loop and move to next iteration.

    print(i+1,end=" ")
    if(i==44): #stop the loop
        break
    i = i + 1

while(True):
   inp = int(input("Enter any number\n"))
   if(inp>100):
      print("Congratulations you have entered number greater than 100\n")
      break
   
   else:
      print("Try again")
      continue