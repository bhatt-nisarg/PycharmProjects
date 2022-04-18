#static method is used to only print
# in this practical we show that how to use class method as alternative constructor
# how to make instance using class method

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return  f"Nmae is {self.name}. Salary is {self.salary} and role is {self.role}"

    """class method"""
    # we use decorators
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


    """ @@@@@@static method"""
    @staticmethod
    def nbm(string):
        print(f"this is nisarg he is {string}")
        return "nb capital"



harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")
#if we want to write like this or we have date in this way then how to print
#then we use class method and alternative constructor
nisarg =Employee.from_dash("nisarg-453-ceo")
#print(nisarg.salary)

#static method run
nisarg.nbm("clever")