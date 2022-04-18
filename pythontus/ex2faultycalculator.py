#Exercise 2
#Faulty calculator
#design a calculator which will correctly solve all the problems excepts the following ons:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
#your program take operator and the two numbers as input from and them returm the result



operator = input("select operator\n +.addition\n -.substitution\n *.multiplication\n /.division\n")
num1 = int(input("enter the first number\n"))
num2 = int(input("enter the second number\n"))
if num1 == 45 and num2 == 3 and operator == '*':
    print("555")
elif num1 == 56 and num2 == 9 and operator == '+':
    print("77")
elif num1 == 56 and num2 == 6 and operator == '/':
    print("4")
elif operator == '+':
    addition = num1+num2
    print(addition)
elif operator == '-':
    subtraction = num1-num2
    print(subtraction)
elif operator == '*':
    multiplication = num1*num2
    print(multiplication)
elif operator == '/':
    division = num1/num2
    print(division)
