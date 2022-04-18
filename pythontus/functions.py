#sum function built in function
a = 9
b = 8
c = sum((a, b))
print(c)

#user defined function

def function1():
    print("you are in function 1")

function1()

def function(a, b):
    print("good to see")
    #print(a+b)
    return  a+b
c = function(1, 2)
print(c)


# doc string :in function first line is call doc string it use to know about the function
def function2(a, b):
     """This is a function which will calculate average of two numbers"""

     average = (a+b)/2
     #print(average)
     return average

#to run docstring below it syntex
print(function2.__doc__)
#function2(4, 5)