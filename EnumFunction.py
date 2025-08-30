L1 = ["Bindi", "Aloo", "chopsticks", "chowmein"]
'''
i=1
for item in L1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i+=1

    '''
for index,item in enumerate(L1):  #Enumerate function takes index and item and adds a counter to each item in a list or other iterable.
    if index%2==0:
        print(f"Jarvis please buy {item}")

