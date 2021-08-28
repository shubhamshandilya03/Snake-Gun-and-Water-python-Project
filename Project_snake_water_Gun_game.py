import random
# Snake,Water,Gun or Rock,Paper,Scissor Games....


def Game(comp, you):
    if(comp == you):
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("Computer's Turn:Select Snake(s),Water(w) and Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("Your Turn:Select Snake(s),Water(w) and Gun(g)?")
a = Game(comp, you)
print(f"Computer Chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is a Tie!!!")
elif a:
    print("Congratulations,You Won!!!")
else:
    print("Sorry,You Loose the game!!!")
