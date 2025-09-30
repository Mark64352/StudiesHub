print("Welcome to City Clearance!")

for _ in range(1000):
    print("Please provide 5 cities.")
    print()

    cities = []

    for i in range(5):
        city = input(f"Enter city {i+1}: ")
        cities.append(city)

    print()
    print("Here are the cities you entered:")
    for city in cities:
        print(city)
    print()

    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    print()

    if try_again != "yes":
        print("Thanks for using City Clearance! Goodbye.")
        break
