"""*******map filter Reduce in python ***********"""
#
# map(function, iterable)
# A map function takes two parameters:
#
# First one is the function through which we want to pass the items/values of the iterable
# The second one is the iterable itself
""" ######################## map function #####################"""
#1 st method is map function
# number = ["3", "12", "05"]

#number[2] = number[2] + 1 # its give error because we cant do operations like  add in string

#then we can do write like this


# for i in range(len(number)):
#     number[i] = int(number[i])
#
# number[2] = number[2] + 1
# print(number[2])

#  how to write this function in one line
##then we use function map
#this is the method of map function

# number = ["3", "12", "05"]
#
#
# number = list(map(int, number))#this map is first argument is for what type to convert and second argument is a who function to convert
# number[2] = number[2] + 1
# print(number[2])



#lets define a function for use map like below

# def sq(a):
#     return a*a
#
# num = [2,3,4,5,6,7,8,9]
# square = list(map(sq, num))
# print(square)

""" if we dont want to use function then we can also use one liner function lamdaa """

# num = [2,3,4,5,6,7,8,9]
# square = list(map(lambda x:x*x, num))
# print(square)
#
""" this is second program of map function """
# def square(a):
#     return  a*a
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
# # this program is writen x(i) value inthis it written on square and cube value
#


"""############# end of map explaination *************"""



"""$$$$$$$ Filter Function $$$$$$"""
"A filter function in Python tests a specific user-defined "
"condition for a function and returns an iterable for the "
"elements and values that satisfy the condition or, in other words, return true."

# filter function is use of filter

# list_1 = [1,2,3,4,5,6,7,8,9]
#this is use with function
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# print(gr_than_5)

#this is use with lamda function
# gr_than_5 = list(filter(lambda x:x>5, list_1))
# print(gr_than_5)
#filter function is a filter the number using filtering technique


""" ************ filter function end**************"""


""" *****_________________Reduce function _____________******"""

# reduce function starting
#reduce function is part of functools
from functools import reduce
#
# list1 = [1,2,3,4]
# num = 0
# for i in list1:
#     num = num + i
# print(num)

#more pythonic way to write this
#it is use to reduce the line of code

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
# first argument is what operation or function we want to add and second argument is a where we wat to use
print(num)