import random
total = 0
dice = int(input("How many dice to roll: "))
for n in range(dice):
    roll = random.randint(1, 6)
    total = total + roll
print(f"Sum of the dice: {total}")

