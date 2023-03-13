numbers_F = [5, 2, 5, 2, 2]
numbers_L = [2, 2, 2, 2, 5]

for number in numbers_L:
    string = ""
    for item in range(number):
        string += "X"
    print(string)