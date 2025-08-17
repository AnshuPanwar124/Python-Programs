list1 = ["Harry","Larry","Carry","Marie"]

for item in list1:
    print(item)

list2 = [["harry",1],["Larry",2],["Carry",3],["Marie",4]]

for item,lollipop in list2:
    print(item, "and lolly is",lollipop)

dict1 = dict(list2)
print(dict1)

for item,lollipop in dict1.items():  #Items function gives all the items present in dictionary
    print(item, "and lolly is",lollipop)

for item in dict1:
    print(item)


items = [int,float,"harry",5,3,44,56,78,9,233,45,76,89,20,30,40,50]

for item in items:
    if str(item).isnumeric() and item>6:
      print(item)

