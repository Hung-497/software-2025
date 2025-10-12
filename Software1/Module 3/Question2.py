ab = str(input("Enter the cabin class (LUX, A, B, or C): "))
if ab == "LUX":
    print("Upper-deck cabin with a balcony.")
elif ab == "A":
    print("Above the car deck, equipped with a window.")
elif ab == "B":
    print("Windowless cabin above the car deck.")
elif ab == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
