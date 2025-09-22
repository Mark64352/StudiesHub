print(f"I will help you convert inches to centimeters.")
print()
while True:
    inches = float(input("Enter value the inches: "))
    if inches < 0:
        print(f"\033[1;31;47mThe value cannot be negative.\033[0m")
        break
    cm = inches * 2.54
    print(f"The conversion of {inches} inches is {cm:.2f} in centimeters.")
    print ()
