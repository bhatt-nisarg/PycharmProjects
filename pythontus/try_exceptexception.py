#this is simple program
#num1 = int(input("Enter num 1\n"))
#num2 = int(input("Enter num 2\n"))
#print("The sum of these two number is", num1+num2)
#***end of simple program***


#using exception write program

num1 = input("enter nume 1\n")
num2 = input("enter num 2\n")

"""in this case we write string or charactor then 
   its an error of type error of convert string to int then
   we use exception handling mechanism for except exception"""
try:
    print("the sum of two number ", int(num1)+int(num2))
except Exception as e:
        print(e)
#it is use for except exception
# it is use in internet activity more and to continue the program

print("this is verry importanat line")