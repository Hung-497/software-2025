import random
def roll_dice(num):
    dice = random.randint(1,num)
    while dice != num:
        print(dice)
        dice = random.randint(1, num)
    print(dice)
    return

num = input("The number of sides: ")
roll_dice(int(num))