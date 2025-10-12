def get_season(month):
    seasons = {12: "December", 1: "January", 2: "February",
               3: "March", 4: "April", 5: "May",
               6: "June", 7: "July", 8: "August",
               9: "September", 10: "October", 11: "November"}
    return seasons.get(month)

name = int(input("Enter the number of a month (1-12): You entered: "))
print(name)
if 0 < name < 3 or name == 12:
    print("The season is winter.")
elif 3 <= name <= 5:
    print("The season is spring.")
elif 6 <= name <= 8:
    print("The season is summer.")
elif 9 <= name <= 11:
    print("The season is autumn.")
else:
    print("Please enter a number between 1 and 12.")