f = open("anshu.txt","rt")  #read and text by default
#print(f.readline())     #print line by line
#print(f.readline())
#print(f.readline())
#content  = f.read(3)      #will read 3 character
#print(content)

#content  = f.read(3)      #will read next 3 character
#print(content)

#content  = f.read()

'''for line in f:              Print whole file contents
    print(line, end="")''' 

"""for line in content:        Print character by character            
    print(line) """

print(f.readlines())  #Print list of lines



f.close()     

