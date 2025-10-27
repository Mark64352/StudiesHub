def odds_removed (numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

nums = [1, 4, 15, 17, 21, 24, 27, 28, 32]
cut_down = odds_removed(nums)
print("Original list:", nums)
print("List without odd numbers:", cut_down)
