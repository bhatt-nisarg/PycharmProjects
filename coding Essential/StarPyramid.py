# this program to make pattern of * Pyramid
"""
            *
           ***
          *****
         *******
"""

N = int(input("Enter element"))
i=1
while i <= N:
    spaces = 1
    while spaces <= N-i:
        print(" ", end="")
        spaces = spaces+1
    star = 1
    while star <= 2*i-1:
        print("*", end="")
        star = star+1
    print()
    i = i+1