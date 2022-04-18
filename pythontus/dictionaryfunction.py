#Dictionary is nothing but key value pairs

d1 = {}
print(type(d1))

#second
d2 = {"Nisarg":"pizza", "vivek":"dhosa", "rucha":"maggie",
      "kardam":{"A":"pizza", "B":"pumjabi"}}

print(d2["Nisarg"])
print(d2["kardam"]["A"])
#to add items
d2["help"] = "chineese"
print(d2["help"])
#d3=d2 is not a coppy of function if you delete name in d2 then also delete from d3 automatically
d3 = d2.copy()
del d3["Nisarg"] #del means delete
print(d3)

print(d2.get("vivek"))
print(d2.update({"kp":"frenchfrise"}))
print(d2)

print(d2.keys()) #it shows keys of dictionary
print(d2.items()) #it shows item in ditionary


