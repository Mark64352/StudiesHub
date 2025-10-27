def gallons_conversion(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("Enter gasoline amount in gallons (negative to stop): "))
    if gallons < 0:
        break
    liters = gallons_conversion(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters")

print("Conversion done.")
