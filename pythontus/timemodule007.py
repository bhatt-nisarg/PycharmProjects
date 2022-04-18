#time module
# """ time module is use for calculate execution time"""
#import  time
# initial = time.time()
# print(initial)
# k = 0
# while(k<15):
#     print("this is NB Capital")
#     k+=1
# print("while loop ran in",time.time(), "seconds")
#
# initial2 = time.time()
# for i in range(15):
#     print("this is NB Capital")
#
# print("for loop is ran in", time.time()-initial2,"seconds")
#


# if initial2>initial:
#     print("while loop execute first")
#
# else:
#     print("for loop execute first")

# this function give local time
import  time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)


#function time.sleep
#it is use to sleep the execution for few seconds

import  time
initial = time.time()
print(initial)
k = 0
while(k<15):
    print("this is NB Capital")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time(), "seconds")

initial2 = time.time()
for i in range(15):

    print("this is NB Capital")
    time.sleep(2)
print("for loop is ran in", time.time()-initial2,"seconds")
