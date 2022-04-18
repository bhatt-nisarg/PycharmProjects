#initialy decide one number
#then take value from users
#then the value is big from the initialy value then gave condition to guess the number


n = 12
var = 1
while(var<10):
    var = int(input("guess the number\n"))
    if var < n:
        print("small number you have entered")
        continue
    elif var > n:
        print("big number you have entered")
        continue
    elif var == n:
        print(" Hurrey! you guess the correct number")
        break
    guess = guess + 1

if(var>9):
    print("Game Over")

