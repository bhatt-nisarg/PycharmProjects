"""Pattern Printing
        Input = Integer n
        Boolean = True or false

        if boolean is true then print this pattern for n
        *
        * *
        * * *
        * * * *
        if boolean is false then
        * * * *
        * * *
        * *
        *
"""
"""
#first method to solve the program
n = int(input("Enter the number\n"))
b = int(input("enter one or zero\n"))
new = bool(b)
if new == True:

          for i in range(1,n+1):
              for j in range(1,i+1):
                print("*", end=" ")

              print()


elif new == False:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")

        print()


"""
"""
#second method to solve th problem


print("Pattern printing")
num = int(input("enter how many rows want you print : "))
print("Enter value 0 or 1")
bool_val = input("1 for True or 0 For False : ")
if bool_val=="1":
    for i in range(0, num+1):       #here i is range is in declaration is 0<i<n+1
        print("*"*i)
if bool_val=="0":
    for i in range(num, 0, -1):  #here -1 is denotes to number to 0 means in decrement form
        print("*"* i)
"""