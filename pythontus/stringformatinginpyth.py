# F strings

#this is simple string
# me = "nisarg"
# a = "this is %s"%me
# print(a)

#this is F string
# me = "nisarg"
# a1 = "capital NB"
# a = "this is %s %s"%(me, a1)
# print(a)

# #dot format
# me = "nisarg"#0
# a1 = "capital NB"#1
# a = "this is {1} {0}"
# b = a.format(me, a1)
# print(b)


""" *** F string ****"""
#it is use for fast string
import math
me = "nisarg"
a1 = "capital NB"
a = f"this is {me} {a1} {math.pow(2,2)}"
print(a)
