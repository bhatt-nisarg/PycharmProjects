f = open("nisarg.txt")  #f is a open function or file handle

#its for read line

#tell function is use for indicate file pointer
#print(f.tell())
print(f.readline())
#if you want to reset file pointer or you want to print one line more time then seek funnction is use
f.seek(7)#you print argument then its start from this chr
#print(f.tell())
print(f.readline())
#print(f.tell())
#print(f.readline())
#print(f.tell())
f.close()