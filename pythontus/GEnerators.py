"""
  # iterate means to traverse any object or class
Iterable - __iter__ or __getitem__()   # this method is used in iterable
Iterator - __next__()
Iteration -
"""

## Generators
# genterators is traverse one

#we traverse only one if it is generators

#def gen(n):
 #   for i in range(n):
  #      yield i       #yield is a one generator
#q=gen(500)
#print(q)
#print(q.__next__())
#print(q.__next__())
#print(q.__next__())
#for i in range(30):
#    print(i)



#where we use generators

#string is iterable and integer is not iterable



h ="Nisarg"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

print()

