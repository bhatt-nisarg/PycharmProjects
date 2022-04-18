#this code is for print number pyramid
"""
             1
           2 3 2
         3 4 5 4 3
       4 5 6 7 6 5 4

Observation:
1. There are n number of rows
2. N-i spaces
3. ith rows-i numbers in the increasing order starting from value i
4. i-1 Numbers in decreasing order
"""

N = int(input("Enter Element: "))
i = 1
while i <= N:
    #for spaceswe have N-i spaces
    spaces = 1
    while spaces <= N-i:
        print(" ", end=" ")
        spaces = spaces+1
    #for printing the value
    value = i
    #we have to print value till count <N
    count = 1
    while count <= i:
        print(value, end=" ")
        value = value+1
        count = count+1
    value = value-2
    count = 1
    while count <= i-1:
        print(value, end=" ")
        value = value-1
        count = count+1
    print()
    i = i + 1