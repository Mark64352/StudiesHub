print("Provide 5 different cities.")
cities = []
for i in range(5):
    city_name = input("Enter a city name: ")
    cities.append(city_name)

print(f"\nfThe cities are:")
for city in cities:
    print(city)