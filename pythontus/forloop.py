#for loops
#to print long list in simple way
print("list output :")
list1 = ["nb", "bn", "nisarg", "nm"]
#declaration
for item in list1:
    print(item)
#to print tuples in for loop
print("tuples output :")
list2 = ("lion", "tiger", "cow", "elephent")
for item in list2:
    print(item)

#to print list of list or tuple of tuple

list3 = [["nb", 1], ["bn", 5], ["nisarg", 12], ["nm", 7]]
print("list of list output:")
#it is a simple way to write list of list
#for item in list3:
#    print(item)
for item, birthdate in list3:
    print(item, "and birthday on", birthdate)
    #it is a same as print(item, birthdate)


#in dictionary type
print("dictionary type list:")
dict1 = dict(list3)
print(dict1)
for item, birthdate in dict1.items():
    print(item, birthdate)
print("only key value")

for item in dict1:
    print(item)


