print("Please enter a number to check if it is even or odd.")
print("Press 0 to stop the program.")
even_count = 0
odd_count = 0
number = []
while True:
    user_value = int(input("Enter a number: "))
    if user_value == 0:
        print("You entered 0. The program will quit.")
        break
    if user_value % 2 == 0:
        print(f"{user_value} is an even number.")
        even_count += 1

    else:
        print(f"{user_value} is an odd number.")
        odd_count += 1

    number.append(user_value)
print("Here is a list the numbers:")
for i in number:
    print(i)
print("The even numbers are:")
print(even_count)
print("The odd numbers are:")
print(odd_count)