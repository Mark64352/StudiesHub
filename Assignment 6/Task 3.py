print("I will assist you with your Airport information.")
airports = {}

while True:
    print("\n1) Enter Airport Information 2) Fetch Airport Information 3) Exit")
    choice = input("Select: ")
    if choice == "1":
        code = input("ICAO code: ")
        name = input("Airport Name: ")
        airports[code] = name
    elif choice == "2":
        code = input("ICAO code: ").upper()
        if code in airports:
            print(airports[code])
        else:
            print("Unknown Airport Code")
    elif choice == "3":
        print("Exit.")
        break