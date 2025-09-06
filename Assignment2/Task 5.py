#input
print(f"Please enter a mass in medieval unit.")
print()
talents = float(input(f"Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

#computation
total_lots = (talents * 20 * 32) + (pounds * 32) + lots
grams = (total_lots * 13.3)
kilograms = int(grams // 1000)
leftover_grams = grams % 1000
print()
#output

print(f"The total mass in medieval unit converted is {kilograms} kilograms and {leftover_grams:.2f} grams.")
