import random

while True:
    print(f"Let's play a guessing game!\nI will pick a number between 1 to 10\nand you have to guess what number it is.\n")

    secret_number = random.randint(1, 10)

    while True:
        guess = (input("Guess a number between 1 and 10: "))
        print()
        try:
            guess = int(guess)
        except ValueError:
            print("Sorry, that's not a number. Please try again!\n")
            continue
        if guess == secret_number:
            print("You guessed it right!\n")
            break
        elif guess < secret_number:
            print("Too low!\n")
        else:
            print("Too high!\n")

    while True:
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        print()
        if play_again in ("yes", "no"): #check if the input matches the systems answer
            break
        print("Invalid choice. Please type 'yes' or 'no'.\n")
    if play_again == "no":
        print("Goodbye!")
        break





