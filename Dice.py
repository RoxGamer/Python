import random

def roll_dice(a):
    x = random.choice(a)
    print("X: ",x)

    if x==1:
        print("\n-----------\n|         |\n|    O    |\n|         |\n-----------")
    elif x==2:
        print("\n-----------\n|    O    |\n|         |\n|    O    |\n-----------")
    elif x==3:
        print("\n-----------\n|    O    |\n|    O    |\n|    O    |\n-----------")
    elif x==4:
        print("\n-----------\n| O     O |\n|         |\n| O     O |\n-----------")
    elif x==5:
        print("\n-----------\n| O     O |\n|    O    |\n| O     O |\n-----------")
    else:
        print("\n-----------\n| O     O |\n| O     O |\n| O     O |\n-----------")

    y = input("To Roll Again Press Y: ")
    print("Y: ",y)
    if (y == "Y"):
        roll_dice(a)
    elif(y == "y"):
        roll_dice(a)
    else:
        print("You have successfully exited the Program")
        exit()

a = [1,2,3,4,5,6]
roll_dice(a)