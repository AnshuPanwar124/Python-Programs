import time
from functools import lru_cache

@lru_cache(maxsize=3)  #saves latest 3 values

def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n 

if __name__ =="__main__":
    print("Now running some work")
    some_work(3)
    some_work(1)  #cache because 3 latest
    some_work(6)  #cache because 2 latest
    some_work(9)  #cache because 1 latest 

    print("done....calling again")
    some_work(3)  # we don't have to wait for 3 sec after caching by using decorator lru_cache
    print("called again")
