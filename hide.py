def get_largest_number(numbers, n):
    numbers.sort()
    return numbers[-n:]



nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(nums)

x = get_largest_number(nums, 2)

print(nums)

print(x)