# anonymous/lambda function
# it is a one liner function
#working
#
# def add(a, b):
#
#     return  a + b
#
# minus = lambda x, y: x-y
# """
# above expression is same like this
# def minus(x, y):
#     return x-y
#
# but it is long
# """
#
# print(minus(9,4))


#lambda use with sort function|
"""if dont want to use function def
then we can use lambda function instead of it"""
# def a_first(a):
#     return a[1]

a = [[1, 4], [5, 6], [8, 23]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)

