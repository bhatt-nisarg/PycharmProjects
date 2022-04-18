f = open("nisarg.txt", "rt")
#content = f.read(3)
#print("1", content)
"""if value is bigger than string then its read whole string from 1 content and ignore the 2"""
#content = f.read(3)
#print("2", content)

"""end the read opration in simple 
    if you want to read content line by line then its in given below"""
#for line by line

#for line in f:
 #    print(line, end="")
"""its for line by line read function"""

# use of readline() function its for read line its get how many time you use read line then its add line to read
#print(f.readline())
#print(f.readline())
#its for read line and next we use readlines function

"""read lines function is use for read ines in list format"""
#print(f.readlines())
f.close()