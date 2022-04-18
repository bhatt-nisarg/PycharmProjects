## enumerate function

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

## its a simple you can try using for loop
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f" jarvis Please buy {item}")
#     i += 1

## using enumerate function

for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis Please buy {item}")