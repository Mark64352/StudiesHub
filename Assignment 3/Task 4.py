print(f"Let's check if a given year is a leap year!")
print()

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year!")
