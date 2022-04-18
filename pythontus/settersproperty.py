""" 70:th video
A property decorator is a built-in function in Python.
Property decorator is a pythonic way to use getters and
 setters in object-oriented programming which comes from the Python
 property class. Theoretically speaking, Python property decorator
  is composed of four things, i.e. getter, setter, deleter and Doc.
   The first three are methods, and the fourth one is a docstring or comment.
"""
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@codewithnb.com

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithnb.com"
    @email.setter
    def email(self,string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")

print(hindustani_supporter.email)
hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithnb.com"
print(hindustani_supporter.fname)

del(hindustani_supporter.email)
print(hindustani_supporter.email)
hindustani_supporter.email = "nisarg.bhatt@codewithnb.com"
print((hindustani_supporter.email))
