import random
def roll_dice():
    n = 0
    dice = random.randint(1,6)
    while dice != 6:
        print(dice)
        n += 1
        dice = random.randint(1, 6)
    print(dice)
    return
roll_dice()