def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "Python is an interpreted language and easy to learn and simple"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("harry")
input("press any key")
search.send("Python")

search.close()

search.send("anshu") # we cannot send after close coroutine.