# with open("nisarg.txt") as f:
#     a = f.read(5)
#     print(a)
# f = open("nisarg.txt", "rt")
# print(f.readlines())# its is a list format of lines
# print(f.readline())
# f.close()
"""with block is use for open python files and in this
    files is close automatically dont requirement of any code"""


"""question of the day"""
#if we open file in out of with block and read file then it will b open or not??
#Answer is No
with open("nisarg.txt") as f:
     print(f.readlines())
open("nisarg.txt")
print(f.readlines())
