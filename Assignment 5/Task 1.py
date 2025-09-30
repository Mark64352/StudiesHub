import random

print("Welcome to Dice Roller Game!")
print()

for _ in range(1000):
    num_dice = int(input("How many dice would you like to roll? "))
    print()
    total = 0
    rolls = []

    for i in range(num_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)
        print(f"Die {i+1} rolled: {roll}")
        total += roll

    print()
    print(f"All rolls: {rolls}")
    print(f"The total sum of your {num_dice} dice is: {total}")
    print()

    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        print()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("Thanks for playing Dice Roller Game! Goodbye.")
            exit()
        else:
            print("Please type only 'yes' or 'no'.")
            print()
