var1 = "100"
var2 = "200"
#its is a string not addition is 300
#but using type casting we chnge a type of variable
print(int(var1) + int(var2))

"""
str()
int()
float()
"""
print(20 * "Hello nisarg\n")
print(10 * str(int(var1) + int(var2)))

#user input
#command line input

print("ENTER YOUR NUMBER")
inpnum = input()

print("you entered", inpnum)
print("your sum", int(inpnum)+10)