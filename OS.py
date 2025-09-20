import os
#print(dir(os)) #Provides list of functions, classes and variables available within the os module.

#print(os.getcwd())

#os.chdir("C://")
#print(os.getcwd())

#f = open("anshu.txt")  #It throws an error because no anshu.txt exists in c folder that is our current directory.

#print(os.listdir("C:/"))


#os.mkdir("this")

#os.makedirs("This/That")  

os.rename("anshu.txt","anshu_p.txt")

print(os.environ.get('Path'))

print(os.path.join("C:/","/harry.txt"))

print(os.path.exists("C://"))

print(os.path.isdir("C://Program Files2"))






