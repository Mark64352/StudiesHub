
import math

print("Welcome to Prime Check!")
for _ in range(1000):
    print(f"""
Give me integers and I’ll check if they’re prime.
You must check at least 3 numbers before deciding to quit.
""")

    count = 0

    for _ in range(1000):
        num = int(input("Enter an integer: "))
        print()

        if num > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f"Yes! {num} is a prime number.")
            else:
                print(f"Nope! {num} is not a prime number.")
        else:
            print("Prime numbers are greater than 1.")

        print()
        count += 1

        if count >= 3:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            print()
            if play_again != "yes":
                print("Thanks for visiting Prime Check! Goodbye.")
                exit()
            else:
                break
