# l = 10  #Global variable read only for local variable
# def function(n):
#
#    # l = 5   #Local
#     m = 7   #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have Printed")
#
# function("this is me")
# #print(l)
# #print(m)#we cant print loacal variable in global
# #but global variable print in both


""" *** new method ***"""
#x = 89  quiz part
def nisarg():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

nisarg()
#print(x) #it is make global variable to 88


# quiz     if x = 89 global then what print x