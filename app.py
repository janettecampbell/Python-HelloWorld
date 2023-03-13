numbers = [3, 6, 2, 8, 4, 10]
largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)