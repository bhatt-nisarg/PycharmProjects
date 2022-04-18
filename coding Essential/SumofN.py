#this code is for make sum of n number

N = int(input("Enter N element :"))
i = 1
sum = 0

while i <= N:
    val = int(input())
    sum += val
    i = i+1

print(sum)