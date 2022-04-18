#create list and list name is number is greater then 5
list1 = [ 1, "rahul", 7, "yashesh", 10, "dhaval", 15]

print("number is greater then 5 and in number")

for item in list1:
    if str(item).isnumeric() and item>5:
        print(item)