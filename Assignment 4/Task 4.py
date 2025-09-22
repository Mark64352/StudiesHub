import random

while True:
    print(f"Let's play a guessing game!\nI will pick a number between 1 to 10\nand you have to guess what number it is.\n")

    secret_number = random.randint(1, 10)

    while True:
        guess = (input("Guess a number between 1 and 10: "))
        print()
        if not guess.isdigit():
            print("Sorry, that's not a number. Please try again!\n")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("You guessed it right!\n")
            break
        elif guess < secret_number:
            print("Too low!\n")
        else:
            print("Too high!\n")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    print()
    if play_again != "yes":
        print("Thank you for playing!")
        break



