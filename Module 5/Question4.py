city = input("Enter the name of a city: ")
cities = []
while city != "":
    cities.append(city)
    city = input("Enter the name of a city: ")

print("The cities you entered: ")
for n in cities:
    print(n)
