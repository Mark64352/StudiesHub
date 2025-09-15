print  (f"Nice catch! Please let us know the size of the Zander you caught.")
print()
zander = float(input(f"Enter the length of the Zander in centimeters: "))
print()
if zander < 42:
    print(
        f"Your Zander catch is under the limit length size to be kept. \n"
        f"You are short of {42 - zander} centimeters. \n"
        f"Thus you must release it back immediately to the lake."
    )
else:
    print(
        f"Your Zander catch is {zander} centimeters and meets the legal limit size! \n"
        f"I'll help you cook it!"
    )