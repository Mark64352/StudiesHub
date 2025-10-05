import random
print("Let's roll some dice!")
rolls = int(input("How many dice do you want to roll? "))
total = 0
for i in range(rolls):
    dice_rolled = random.randint (1,6)
    total += dice_rolled
print(total)