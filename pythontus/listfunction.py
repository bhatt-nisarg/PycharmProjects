#list function
food = ["bhaji", "panipuri", "dhosa","bhajiya", 12]

print(food)
print(food[0])
print(food[3])


numbers = [2, 3, 4, 7, 8]
#insert function is used to add number in front
numbers.insert(1, 100)
print(numbers[2])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#this is from reverse function
#this is positive slicing
print(numbers[0:2])
print(numbers[::1])
print(numbers[::3])
#to reverse the list
print(numbers[::-1])
#in negetive slicing dont take value lessthen -1 because it return null list

'''
in this list other function  max min and lenth and other is same as  string '''
numbers.append(7) #you can add the end in any time
print(numbers)

#this is blank list to add numbers
num = []
num.append(12)
num.append(13)
num.append(14)

print(num)

#mutable and immutable function

#tuple is a function same as list its diffrence is parenthesis
tp = (12, 4, 2001)
#tp[1] = 14 #tuple object does not support item assignment
print(tp)

#to have one number then
a = (1,)
print(a)

#to swap numbers

b = 4
c = 12
b, c = c, b
print(b, c)
