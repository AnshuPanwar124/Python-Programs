f1 = open("anshu.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)

else:
    print("this will run only if except is not running")

finally:   #for code cleanup
    print("Run this anyway")
    #f.close()
    f1.close()

print("Important stuff")