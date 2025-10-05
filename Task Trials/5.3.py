print("Let's check if as integer is a prime number. Press Enter to quit.")
while True:
    integer = int(input("Enter a number: "))
    if integer == "":
        print("User pressed quit.")
        break
    elif integer > 1:
        for num in range(2, integer):
            if integer % num == 0:
                print(f"{integer} is not a prime number.")
                break
        else:
            print(f"{integer} is a prime number.")