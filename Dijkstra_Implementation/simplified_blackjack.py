##---import library---##
import random
#--rules--#
print("Try to get the closest to 21. There are no face cards.")
print("If you go over 21 you're out.")
print()
##---setup cards---##
total = 0
#--first card--#
num_1 = random.randint(1,10)
print(num_1)
print()
#--second card--#
num_2 =random.randint(1, 10)
print(num_2)
print()
total = num_1 +num_2
#--total--#
print("Total: " + str(total))
print()
#--hit or stand--#
hit_stand = input("Would you like to hit (h) or stand (s)? ")
if hit_stand == "h":
    num_3 = random.randint(1, 10)
    total += num_3
    print(num_3)
    print("Total: " + str(total))
    print()
    #--hit or stand 2--#
    hit_stand = input("Would you like to hit (h) or stand (s)? ")
    if hit_stand == "h":
        num_3 = random.randint(1, 10)
        total += num_3
        print(num_3)
        print("Total: " + str(total))
        print()
        #--hit or stand 3--#
        hit_stand = input("Would you like to hit (h) or stand (s)? ")
        if hit_stand == "h":
            num_3 = random.randint(1, 10)
            total += num_3
            print(num_3)
            print("Total: " + str(total))
            print()
##--reactions--##
if total > 21:
    print("Bust!")
    print()
if total == 21:
    print("Blackjack!")
    print()
##--opponent setup--#
opponent = random.randint(12, 27)
print("Your opponent got " + str(opponent))
print()
##--reactions to opponent--##
if opponent > 21:
    print("Bust!")
    print()
if opponent == 21:
    print("Blackjack!")
    print()
##--determining the winner--##
if total == 21:
    if opponent == 21: #if both you and the opponent got 21, you tie
        print("Tie!")
    else:
        print("You won!") #if only you got 21 you win
if total < 21:
    if opponent == 21: #if you got less than 21, but your opponent got 21, you lose
        print("You lost!") 
    elif opponent > 21: #if you didnt go over 21 but your opponent did, you win
        print("You won!")
    elif total > opponent: #in the case you got less than 21, but your opponent got less, you win
        print("You won!")
    elif total < opponent: #in the case you and your opponent get less than 21, but your opponent got more, you lose
        print("You lost!")
if total > 21:
    if opponent > 21: #if both you and your opponent bust, you tie
        print("Tie!")
    else: # if your opponent doesnt bust but you did, you lose
        print("You lost!")

