name = input("Enter biological gender (male/female): ")
name = name.lower()
value = float(input("Enter hemoglobin value (g/l): "))

if name == "male":
    if 134 < value < 167:
        print("Your hemoglobin is normal.")
    elif value < 134:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
elif name == "female":
    if 117 < value < 155:
        print("Your hemoglobin is normal.")
    elif value < 117:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")
