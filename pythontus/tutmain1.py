##this video is about use of main function
##here two files there are one is tutmain1 and tutmain2 is file using main function
##if_name__ ==__main__usage&necessity

def printnb(String):
    return f"Ye String nb ko de de thakur {String}"
def add(num1, num2):
    return num1 + num2 + 5

print("and the name is", __name__)
if __name__ == '__main__':
    print(printnb("nisarg"))
    o = add(4,6)
    print(o)