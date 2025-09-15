print(f"Please enter your biological gender and hemoglobin level (g\\L)")
print()

gender = input("Please enter your gender: ").strip().upper()

if gender == "MALE":
    low_normal = 134
    high_normal = 167

elif gender == "FEMALE":

    low_normal = 117
    high_normal = 155

else:
    print(f"\033[1;31;47mError. Enter your correct biological gender.\033[0m")
    exit()

hemoglobin = float(input("Please enter your hemoglobin level (g\\L): "))

if hemoglobin < low_normal:
    print(f"Your hemoglobin levels are considered \033[1;31mLOW.\033[0m")
elif hemoglobin > high_normal:
    print(f"Your hemoglobin levels are considered \033[1;31mHIGH.\033[0m")
elif low_normal <= hemoglobin <= high_normal:
    print(f"Your hemoglobin levels are considered \033[1;32mNORMAL.\033[0m")

