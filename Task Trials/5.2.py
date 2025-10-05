print("Provide several numbers. Minimum of 5. Press Enter to stop.")
all_numbers = []

while True:
    number = input(f"Enter a number: ")
    if number == "":
        print("Program stopped.")
        break
    number = float(number)
    all_numbers.append(number)

print(f"Here are all the numbers provided: {all_numbers}")
all_numbers.sort(reverse=True)
top_numbers = all_numbers[:5]
print(f"The top 5 numbers are: {top_numbers}")
