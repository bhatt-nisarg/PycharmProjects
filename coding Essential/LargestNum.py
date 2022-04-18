#this code is for finding the largest number of the given three number
def largestNumber():
    A = int(input("Enter A :"))
    B = int(input("Enter B :"))
    C = int(input("Enter C :"))

    if A>=B and A>=C :
        print(A,"is largest")
        return
    if B>=A and B>=C:
        print(B,"is largest")
        return
    else:
        print(C,"is largest")
        return
largestNumber()