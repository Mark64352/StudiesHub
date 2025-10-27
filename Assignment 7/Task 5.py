import math

def pizza_value(diameter, price):
    r = diameter / 2 / 100
    area = math.pi * r * r
    return price / area

diameter_1 = float(input("Pizza 1 diameter (cm): "))
pizza_1 = float(input("Pizza 1 price (€): "))
v1 = pizza_value(diameter_1, pizza_1)
print(f"Pizza 1 price per square meters: {v1:.2f} €/m².")
print()

diameter_2 = float(input("Pizza 2 diameter (cm): "))
pizza_2 = float(input("Pizza 2 price (€): "))
v2 = pizza_value(diameter_2, pizza_2)
print(f"Pizza 2 price per square meters: {v2:.2f} €/m².")
print()
if v1 < v2:
    print("Pizza 1 is cheaper per square meter.")
elif v2 < v1:
    print("Pizza 2 is cheaper per square meter.")
else:
    print("They cost the same per area.")