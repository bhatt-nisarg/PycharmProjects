"""  WHAT IS MULTILEVEL INHERITENCE IN PYTHON"""
"""In multilevel inheritance, a class that is already derived 
from another class is derived by a third class. So in this way
the third class has all the other two former classes' features 
and functionalities."""

"""SYNTEX_===="""
# class Parent1:
#     pass
# class Derived1(Parent1):
#     pass
# class Derived2(Derived1):
#     pass


"""    example of multilevel inheritence """
#
# class level1:
#     def first(self):
#         print('code')
#
#
# class level2(level1):  # inherit level1
#     def second(self):
#         print('with')
#
#
# class level3(level2):  # inherit level2
#     def third(self):
#         print('nisarg')
#
#
# obj = level3()#this is one object is level3 inherit all method
# obj.first()
# obj.second()
# obj.third()

"""  ***PROGRAM OF MULTILEVEL INHERITENCE """
#
# class Dad:
#     basketball =6
#
# class Son(Dad):
#     dance =1
#     basketball = 9
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"
#
# class Grandson(Son):
#     dance =6
#     guitar = 1
#
#     def isdance(self):
#         return f"Jackson yeah!" \
#             f"Yes I dance very awesomely {self.dance} no of times"
#
# darry = Dad()
# larry = Son()
# harry = Grandson()
#
# print(harry.isdance())


"""-------------------its time for small exercise"""
#you have three class below and you will relevent their eachother
# electronic device
# pocket gadget
# phone

#
# class electronicdevice:
#     motor =1
#     computer = 3
#     laptop = 5
#     videogame = 5
#     phone = 10
#
#
# class pocketgadget(electronicdevice):
#     def gadget(self):
#         return f"we have gadget is morethen {self.videogame+self.phone} we happy to say that"
#
#
#
# class phone(pocketgadget):
#     pass
# ob1 = electronicdevice()
# ob2 = pocketgadget()
# ob3 = phone()
# print(ob3.gadget())
