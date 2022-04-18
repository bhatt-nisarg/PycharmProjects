"""**** multiple inheritence &&&&&"""
"""In multiple inheritance a class is derived from more 
than one class i.e. multiple base classes. The child class
 in this case has features of both the parent classes."""


##   EXAMPLE OF MULTIPLE INHERITENCE
# class Base1:
#     def func1(self):
#         print("this is Base1 class")
#
#
# class Base2:
#     def func2(self):
#         print("this is Base2 class")
#
#
# class Child(Base1, Base2):    ##this sequence is required first class is inherit first and after second class
#     def func3(self):
#         print("this is Base3 class")
#
#
# obj = Child()
# obj.func1()
# obj.func2()
# obj.func3()



"""  ###@@@@@ program of multiple inheritence"""

#
# class Employee:
#     no_of_leaves = 8
#     var = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
# #     def printdetails(self):
# #         return f"T Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)
#
# class Player:
#     var = 9
#     no_of_games = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game =game
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Game is {self.game}"
#
# class CoolProgramer(Player, Employee):
##this inherit sequence is required for what to inherit and first
#     language = "C++"
#     def printlanguage(self):
#         print(self.language)
#
# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
#
# shubham = Player("Shubham", ["Cricket"])
# karan = CoolProgramer("Karan",["Cricket"])
# # det = karan.printdetails()
# # karan.printlanguage()
# # print(det)
# print(karan.var)
#
