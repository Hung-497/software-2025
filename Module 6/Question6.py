import math
def calculate_unit_price(diameter, price):
    area = (diameter / 100 / 2)**2 * math.pi
    unit = price / area
    return unit
dia1 = int(input("Enter the diameter of the first pizza (cm): "))
pri1 = int(input("Enter the price of the first pizza (euros): "))
dia2 = int(input("Enter the diameter of the second pizza (cm): "))
pri2 = int(input("Enter the price of the second pizza (euros): "))
print(f"Unit price of the first pizza: {calculate_unit_price(dia1, pri1):.2f} euros/m²")
print(f"Unit price of the second pizza: {calculate_unit_price(dia2, pri2):.2f} euros/m²")
if calculate_unit_price(dia1, pri1) < calculate_unit_price(dia2, pri2):
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")



