#write in file
f = open("nisarg2.txt", "w")
f.write("nisarg is very hardworing")
f.close()

#append is use for joining at end append is for a
f = open("nisarg2.txt", "a")
f.write("nisarg is very hardworing")
f.close()

#if you want a howmany charachtor in this file then
f = open("nisarg2.txt", "w")
a = f.write("nisarg is very hardworing")
print(a)
f.close()

#Handle Read and write both then use r+ mode
f = open("nisarg2.txt", "r+")
print(f.read())
f.write("\nwelcome")
#it is for reading and writing in file at same 
