"""*****join function********"""

l2 = ["John", "Cena", "Randy", "Orton",
      "Sheamus", "Khali", "jinder mahal"]

##how to join function using code like this
#john and cena and randy and  etc...
# using and how to join


#first method
# for item in l2:
#     print(item, "and", end=" ")
# print("other wwe superstar")

##this is second method
a = " and ".join(l2)
# we also join with "," like this a= ",".join(l2)
print(a, "othe wwe superstar")

