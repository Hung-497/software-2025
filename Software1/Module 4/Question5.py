round = 0
user = "python"
password = "rules"
while round < 5:
    smth = input("Enter username: ")
    smbd = input("Enter password: ")
    if smth.strip().lower() == user and smbd.strip().lower() == password:
        print("Welcome")
        break
    round = round + 1
    if round < 5:
        print("Incorrect username or password. Please try again.")
else:
    print("Access denied")