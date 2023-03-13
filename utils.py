def find_max(input_list):
    max_number = input_list[0]
    for number in input_list:
        if number > max_number:
            max_number = number
    return max_number
