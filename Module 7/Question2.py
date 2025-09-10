names = set()
while True:
    name = input('Enter your name: ')
    if name == "":
        print("OK")
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
for n in names:
    print(n)
