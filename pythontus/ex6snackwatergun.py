""" it is a game to play game 10 time and choose snake water gun out of these keyword """
import random

chance = 10
win_user = 0
win_comp = 0
l1 = ("s", "w", "g")
print("\t \t snake water gun gaming \n \n")
choice = random.choice(l1)


win = 1

while(win<11):
     print("Enter random from these snake water gun\n")
     user1 = input("s for snake \nw for water \ng for fun\n")
     print(user1)
     print(choice)
     if user1 == choice:
                    print("you won")
                    win_user = win_user + 1
                    win = win + 1
                    continue

     else:
                    print("computer wins")
                    win_comp = win_comp + 1
                    win = win + 1
                    continue




if win_user>win_comp:
        print("User wins the game score is" + " " + str(win_user))
elif win_user<win_comp:
        print("computer win this game by score is" + " " + str(win_comp) )

elif win_user==win_comp:
    print("its gone a tie and the svore of both is" + " " +  str(win_user))
