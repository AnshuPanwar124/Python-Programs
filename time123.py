import time

initial = time.time()

k=0
while(k<45):
    print("Anshu is good girl")
    time.sleep(2)  #It hault the program for 2 sec
    k+=1
print("While loop ran in", time.time()-initial, "Seconds")

initial2 = time.time()
for i in range (45):
    print("Abhishek is handsome boy")
print("For loop ran in", time.time()-initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)