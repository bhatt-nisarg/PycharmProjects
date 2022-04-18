# this code is for to check whether the number is prime or not
def PrimeCheck():
    N = int(input("Enter the element"))
    i = 2
    while i <= N-1:
        if N % i == 0:
            print(N,"is Not Prime")
            return
        i = i+1
    print(N,"Is Prime Number")
    return
PrimeCheck()