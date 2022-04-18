#Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represents dunder methods.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):#its method call dunder init  it is a special constructor when call any object it is automatically run
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):    # its method is use to operator overloading and its called dunder add
        return self.salary + other.salary

    def __truediv__(self, other):  # this is division dunder method
        return self.salary / other.salary

    def __repr__(self):   # this method is use
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
#emp2 =Employee("Rohan", 5, "Cleaner")
#print(emp1 + emp2) #if we want to add this two employee  then dunder add method is used
print(str(emp1))
