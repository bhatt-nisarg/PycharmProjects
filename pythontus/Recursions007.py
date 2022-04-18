#recursions use
#its use function in function
#base
# def print2(str1):
#    # print2(str1)
#     print("This is"  + " "  +str1)
#
# print2("nisarg")


#factorial logic
"""
n! = n * n-1 * n-2 * n-3 .......1
#above line is also write like this
n! = n * (n-1)!
"""
""" ....itis a simple def"""
# def factorial(n):
#      """
#
#      :param n : Integer
#      :return: n * n-1 * n-2 * n-3.........1
#     """
#     pass



#factorial program
#iterative approch
#
# def factorial_iterative(n):
#     """
#
#        :param n : Integer
#        :return: n * n-1 * n-2 * n-3.........1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
#
# #factorial using recursive method
# def factorial_recursive(n):
#     """
#
#        :param n : Integer
#        :return: n * n-1 * n-2 * n-3.........1
#     """
#     if n == 1:
#        return 1
#     else:
#        return n * factorial_recursive(n-1)
#
# """ ***** Logic *****
# suppose we have n =5 then its factorial id
#
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 factorial_recursive(2)
# 5 * 4 * 3 * 2 factorial_recursive(1)
# and we have value of n == 1
# then its goto th if and return 1
# 5 * 4 * 3 * 2 * 1 = 120
# its a answer
# (:
# """
#
# number = int(input("Enter Number\n"))
# print("Factorial Using Iterative Method",factorial_iterative(number))
# print("Factorial Using Recursive Method",factorial_recursive(number))


### quiz of fibonanci series

#0 1 1 2 3 5 8 13 .....
def fibonacci(n):

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return  fibonacci(n-1) + fibonacci(n-2)
n = int(input("enter number\n"))
print(fibonacci(n))