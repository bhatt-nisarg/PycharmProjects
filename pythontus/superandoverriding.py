# over riding

class A:
    classvari = "I Am A class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class a constructor"
        self.classvari = "Instance variable in class A"
        self.special = "this is spacial"
class B(A):
    classvari = "I Am in class B"


    def __init__(self):
   #     super().__init__()
        self.var1 = "i am inside class B constructor"
        self.classvari = "Instance variable in class B"
        super().__init__()
        print(super().classvari)
a = A()
b = B()
print(b.special, b.classvari, b.var1)