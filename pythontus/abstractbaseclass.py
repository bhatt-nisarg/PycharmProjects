# “An abstract method is a method defined inside an abstract class.”

# abstract method is used to forcefully do operation in other class

""" syntex for abc meta class"""
# from abc import ABC, abstractmethod
# Class MyClass(ABC):
#       @abstractmethod
#       def mymethod(self):
#             #empty body
#             pass

#  practical


# from abc import ABCMeta, abstractmethod  this is for version 3.4 below
from abc import ABC, abstractmethod  # this is for python version 3.4 upper

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# we cant create abstract base class object
#myabstract = Shape()

