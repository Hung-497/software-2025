num = []
number = input("Enter a number: ")

while number != "":
    num.append(float(number))
    number = input("Enter a number: ")

num.sort(reverse=True)
print("The greatest numbers in descending order:")
for n in num[:5]:
    print(n)