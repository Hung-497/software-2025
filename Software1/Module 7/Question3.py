def menu():
    menu = {1: "1. Enter a new airport",
            2: "2. Fetch airport information",
            3: "3. Quit"}
    print("\nAirport Data Management")
    for k in menu:
        print(menu[k])
    return menu
def system():
    airports = {}
    while True:
        option = input("Please choose an option (1-3): ").strip()
        if option == "1":
            code = input("Enter the ICAO code: ").strip().upper()
            name = input("Enter the airport name: ")
            airports[code] = name
            print(f"Airport {name} with ICAO code {code} has been added.")
            menu()
        elif option == "2":
            code = input("Enter the ICAO code: ").strip().upper()
            if code in airports:
                print(f"The airport with ICAO code {code} is {name}.")
                menu()
            else:
                print(f"No airport found with ICAO code {code}.")
                menu()
        elif option == "3":
            print("Thank you for using the Airport Data Management system. Goodbye!")
            break
        else:
            break
    return system
menu()
system()