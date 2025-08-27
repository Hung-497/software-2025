value = float(input("Enter length in inches (negative value to quit): "))
while value >= 0:
    cm = value * 2.54
    print(f"{value:.1f} inches is {cm:.2f} centimeters")
    value = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")
