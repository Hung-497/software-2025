import random

guess = random.randint(1, 10)
user = None
while guess != user:
    user = int(input("Guess a number (1-10): "))
    if user < guess:
        print("Too low")
    elif user > guess:
        print("Too high")
    else:
        print("Correct")

