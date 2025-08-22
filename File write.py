f = open("anshu2.txt", "w")
f.write("anshu bhut achi hain")  #will replace existing contents of a file and rewrite this.

f = open("anshu2.txt", "a")
a=f.write("anshu bhut achi2 hain\n")  #will add to the existing contents of a file.
print(a)  #print length of char written.

f = open("anshu2.txt", "r+")  #Handle read and write both
print(f.read())
f.write("anshu is good girl she wants to learn python")

f.close()

