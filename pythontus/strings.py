mystr = "nisarg is good boy"
print(len(mystr))
print(mystr[6])
print(mystr[0:6])
print(mystr[0:6:2])
print(mystr[0:])
print(mystr[:6])
print(mystr[0::2])
print(mystr[::])
#in above state ment it takes value automaticaly is given as below
print(mystr[0:19:1])
print(mystr[::9])
print(mystr[::999])

#negative index
print(mystr[-4:-2])
#above is sem as below
print(mystr[14:16])
#to reverse a string
print(mystr[::-1])
print(mystr[::-2])
#new functions
print(type(mystr))
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("boy"))
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("good", "bad"))