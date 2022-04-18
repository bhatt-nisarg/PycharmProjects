# args or kwargs

def function_name (a, b, c, d):
    print(a, b, c, d)

function_name("Harry", "rohan", "Skillf", "shivam")

#if we want to add name then
# args
#
# def funargs(*args):
#     print(type(args))
#     for item in args:
#         print(item)
#
#
# har = ("nb", "harry", "skillf", "Hammad", "shivam")#if you wnt to add namethen you can add
# funargs(*har)

#noramal with args

#
# def funargs(normal, *args):
#     print(type(args))
#     print(normal)
#     for item in args:
#         print(item)
#
# har = ("nb", "harry", "skillf", "Hammad", "shivam")
# normal = ("this is the normal written by:")
# funargs(normal, *har)

#we cant chance place after args then it is an error
#we cant write like this error- (*args, norma)

# kwargs
def funargs(normal, *args, **kwargsnb):
    print(type(args))
    print(normal)
    for item in args:
        print(item)

    print("now we awarded our super heroes(:")
    for key, value in kwargsnb.items():
        print(f"{key} is a {value}")

har = ("nb", "harry", "skillf", "Hammad", "shivam")
normal = ("this is the normal written by:")
kw = { "nisarg": "chef", "kardam":"hardworking", "shivam":"monitor"}#if we want to add items then add in end
funargs(normal, *har, **kw)
