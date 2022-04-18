# def function1():
#     print("Subscribe now")
#
# func2 = function1()
#
# del function1
# func2

#
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a = funcret(0)
# print(a)

# def executor(func):
#     func("this")
#
#
# executor(print)



###decorator function
#it is use to decorate the function

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_nb():
    print("nb is a good boy")

#who_is_nb = dec1(who_is_nb)#this is same as@dec1
who_is_nb()