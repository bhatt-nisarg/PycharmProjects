#dimond shape problem
#syntex example
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D( B, C ):
#     pass


#   PRACRICAL

class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
     def met(self):
        print("This is a method from class C")

class D(C, B):
     def met(self):
        print("This is a method from class D")



a = A()
b = B()
c = C()
d = D()

d.met()

#if we have one method in class b and class a then it confused what should do print
# this problem call dimond shape problem
