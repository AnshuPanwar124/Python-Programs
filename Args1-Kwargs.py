def funargs(normal,*args, **kwargs):  #It takes arguments as a tuple.
    print(normal)
    for item in args:
        print(item)

    for key,value in kwargs.items():
        print(f"{key} is a {value}")

    print(type(args))
    print(args[0])

har = ["Harry", "Rohan", "SkillF", "Hammad", "Shivam", "Anshu"]
normal = "this is a normal"
kar = {"Rohan":"Monitor", "Harry":"Fitness Instructor","Anshu":"beautiful girl"}
funargs(normal,*har,**kar)

    
