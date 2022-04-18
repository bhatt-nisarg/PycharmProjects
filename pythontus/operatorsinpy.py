# operators in python:

# Arithmatic operators::
print("5 + 6 is", 5+6)
print("5 - 6 is", 5-6)
print("5 * 6 is", 5*6)
print("5 / 6 is", 5/6)
print("5 // 6 is", 5//6)#its gave divide in floor division means give in int
print("5 ** 3 is", 5**3)#its give a exponantial operators 5 to the power of 6
print("5 % 5 is", 5%5)#its give modulo its give reminder
#Assignment operators
#assignment operator is use to assign value
print("Assignment operators")
x = 5
print(x)
x +=7
print(x)
#x -=7
#x /=7
#comparision operators
#it is get comparision between two numbers
i = 8
print(i == 5)
#it is comarision operators
print(i != 5)
#ex == != <= >=

#logical operators
#its for logical operation like loogical AND OR NOT ETC
a = True
b = False
#its same as boolean algebra
# a b a and b(a*b) | a or b(a + b) true = 1 false = 0
# 1 1 1            |   1
# 1 0 0            |   1
# 0 1 0            |   1
# 0 0 0            |   0
print(a and b)
print(a or b)
#identity operators
#is or is not
print(5 is 6)
print(a is not b)

#membership operators

#membership operator is a in list or not in type of operators
list = [3, 3,2, 2,39, 33, 35,32]
print(3 in list)
print(35 not in list)

#Bitwise operators

#it deal with binary operators

#0 - 00
#1 - 01
#2 - 10
#3 - 11

print(0 & 1) #it same as and op.
#its logic
#  0 - 00  & 1 - 01
#00
#01
#00
print(0 | 3) #it same as or op.
#its logic
#00
#11
#or logic
#11

