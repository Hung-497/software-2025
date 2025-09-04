def gallons_to_liters(gallon):
    n = 0
    while gallon >= 0:
        n = gallon * 3.785
        print(f'{gallon:.1f} American gallons is {n:.2f} liters.')
        gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
    else:
        print("Program finished.")
    return
gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
gallons_to_liters(gallon)