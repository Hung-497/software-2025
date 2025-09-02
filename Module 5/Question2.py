num = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    num.append(float(number))

num.sort(reverse=True)
print("The greatest numbers in descending order:")
for n in num[:5]:
    print(n)