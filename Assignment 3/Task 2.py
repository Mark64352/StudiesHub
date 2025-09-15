print(
    f"Welcome aboard to Azure Symphony Cruise Ship!\n"
    f"To assist you to your cabin, could you please provide us your cabin class."
)

print()

cabin_class = input("What is your cabin class?: ").strip().upper()

if cabin_class == "LUX":
    print(
        f"Welcome aboard to Lux cabin!\n"
        f"You will have an upper-deck cabin with a balcony."
    )
elif cabin_class == "A":
    print(
        f"Welcome aboard to A- cabin!\n" 
        f"Your cabin will be above the car deck with a window."
    )
elif cabin_class == "B":
    print(
        f"Welcome aboard to B- cabin!\n"
        f"Your cabin will be above the car deck without a window."
    )
elif cabin_class == "C":
    print(
        f"Welcome aboard to C- cabin!\n"
        f"Your cabin will be below the car deck without a window."
    )

else:
    print(f"\033[1;31;47mINVALID CABIN CLASS\033[0m")