smallest = ""
largest = ""
number = input("Enter a number (or press Enter to quit): ")
while number != "":
    x = float(number)
    if smallest == "" or x < smallest:
        smallest = x
    if largest == "" or x > largest:
        largest = x
    number = input("Enter a number (or press Enter to quit): ")
if smallest != "":
    print(f"Smallest number: {smallest:.1f}")
    print(f"Largest number: {largest:.1f}")