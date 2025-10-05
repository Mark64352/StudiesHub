print("Enter several names and I will list them to you! Press Enter to stop.")
name_all = set()

while True:
    name_user = input("\nEnter a name: ")
    if name_user == "":
        break
    elif name_user in name_all:
        print("You have already entered that name.")
    else:
        print("Name added.")
        name_all.add(name_user)

print("\nYou entered these unique names:\n")
for name in name_all:
    print(name)