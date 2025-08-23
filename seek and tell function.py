f = open("anshu.txt") 
#print(f.tell())            #return the current position of the file pointer
print(f.readline())
f.seek(10)
#f.seek(0)       #reset pointer (Change position of file pointer) to index mentioned inside that function.    
#print(f.tell()) 
print(f.readline())
f.seek(22)
#print(f.tell()) 
print(f.readline())

f.close()
