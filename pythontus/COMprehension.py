#  wroting code in more pythonic way
# it is use to create dictionaries set list and generators in one line

"""   **** List comprehension"""

# simple list
listA = []
for a in range(50):
    if a%5==0:
        listA.append(a)

# comprehension list
 listA = [a for a in range(50) if i%5==0]


"""  **** set comprehension"""

alpha = { alpha for alpha in ["a","a","b","c","d","d"]}

#output is {'a','b','c','d'}   only one time print item in set

"""  **** dictionary comrehension"""

# normal dictionary

Normaldict = {
    0:"item0",
    1:"item1",
    2: "item2",
    3:"item3",
    4 :"item4",
}

#comprehension Dictionry

Compdict = {i:f"Item{i}" for i in range(5)}


""" **** generator comprehension"""

#simple generator

def gen(n):
    for i in range(n):
        yield i

a = gen(5)
print(a.__next__())

#comprehension generators

gen = (i for i in range(n))
a = gen(5)
print(a.__next__())



### quiz of comprehension


list = []
for i in range(10):
        val = input()
        list.add(val)
print("which comprehension ")
print(f"choice{1} list comprehension")
print(f"choice{2} set comprehension")
print(f"choice{3}  dicitonary comprehension")
print(f"choice{4} generator comprehension")
c = int(input())

swich(c):
     c=1:
        listcom = [val for val if range(list)]
        print(list)
     c==2:
        setcom ={val for val if range(list)}
        print(setcom)
    c==3:
        dictcom = {}

