# class  method

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





harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

#Employee.no_of_leaves= 100
#how to change the no of leaves using function
#then we use class method
harry.change_leaves(34)
#this methhod is allow all members to change the numbers of leaves
print(harry.no_of_leaves)