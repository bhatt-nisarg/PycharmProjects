#Introspection can be said as the ability to recognize the object along with all its details, such as id or location at runtime. One of the most basic introspects we came across many times earlier is type().
#syntax
"""
type(object) - used to see type of our object
id(object) - id provides a id allocated to the particular object it is unique for every object
o = MyClass()
print(dir(0)) - its returns a list of attributes and method assosiated with an object

"""



class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)
o = "this is a string"
# print(dir(skillf))
# print(id("that that"))

import inspect
print(inspect.getmembers(skillf))


