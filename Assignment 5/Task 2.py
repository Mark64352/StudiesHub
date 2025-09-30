print("Welcome to Number Collector Supreme!")
for _ in range(1000):
    print(f"""
You must enter at least 5 numbers.
After that, you can press Enter without typing anything to stop.
""")

    numbers = []

    for _ in range(1000):
        entry = input("Enter a number (or press Enter to quit): ")
        if entry == "":
            if len(numbers) < 5:
                print("You need at least 5 numbers. Keep going!")
                continue
            else:
                break
        numbers.append(int(entry))

    print()
    numbers.sort(reverse=True)
    print("Here are the five greatest numbers you entered:")
    for n in numbers[:5]:
        print(n)
    print()

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    print()
    if play_again != "yes":
        print("Thanks for playing Number Collector Supreme! Goodbye.")
        break