#class name first charachtor should be capital it is good habbit
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"
#print(harry.salary)
#print(harry.no_of_leaves)

"""#####we cant chage the properties of main class from their object """
""" we cant change the number of leaves with the help of rohan and harry
    but if we want to change then we used Employee"""
# print(Employee.no_of_leaves)
# rohan.no_of_leaves = 10

# print(Employee.no_of_leaves)
#this cant change
#same as we cant change with the help of harry
print(Employee.no_of_leaves)
print(rohan.__dict__)
#dict is use for  return dictionary
rohan.no_of_leaves = 10
#the no of leaves is 10 for rohan
#it means in rohan it makes new variable no_of_leaves of 10
#if we write after rohan then it should contain no of leaves of rohan
print(rohan.__dict__)

print(Employee.no_of_leaves)


# #we used employee
# print(Employee.no_of_leaves)
# Employee.no_of_leaves = 10
# print(Employee.no_of_leaves)
#this make change in no of leaves
