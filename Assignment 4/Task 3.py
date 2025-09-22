print(f"Please provide numbers into the program.\n(To leave a value blank, press ´Enter´)")
print()
number = [] # for storing the values a user puts
while True:
    number_input = input(f"Enter a number: ")
    if number_input == "":
        break #once this breaks, the program starts to move if condition or else!!

    try:
        number_value = float(number_input)
        number.append(number_value)
    except ValueError:
        print("Invalid input. Please enter a number.")
        print()
print()
if number:
    print(f"The system will now provide the smallest and the largest value entered by the user.") #only printing when program goes into the if condi
    print()
    print(f"The smallest value is {min(number)}.")
    print(f"The largest value is {max(number)}.")
else:
    print(f"No numerical values entered.")

