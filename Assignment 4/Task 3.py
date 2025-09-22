print(f"Please provide numbers into the program.\n(To leave a value blank, press ´Enter´)")
print()
number = [] # for storing the values a user puts
while True: #1st step asks first the loop condition until it is not true and goes to the inner if, after the break it goes to the main if,elif and else. (break and exit are different)
    number_input = input(f"Enter a number: ")
    if number_input == "":
        break #once this breaks, the program starts to move if condition or else!!

    try: #so that the system wont crash when input is not a number, it goes to value error and does the prompt
        number_value = float(number_input)
        number.append(number_value)
    except ValueError: #checks and prints when a value is not in numerical form
        print("Invalid input. Please enter a number.")
        print() #goes back to the question loop because these are inside the while loop!
print()
if number: #2nd step after the break in the while loop
    print(f"The system will now provide the smallest and the largest value entered by the user.") #only printing when program goes into the if condi
    print()
    print(f"The smallest value is {min(number)}.")
    print(f"The largest value is {max(number)}.")
else:
    print(f"No numerical values entered.")

