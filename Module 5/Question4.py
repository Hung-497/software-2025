cities = []
# while city != "":
#     cities.append(city)
#     city = input("Enter the name of a city: ")

for i in range(5):
    city = input(f"Enter the name of a city: ")
    i +=1
    cities.append(city)

print("\nThe cities you entered: ")
for n in cities:
    print(n)
