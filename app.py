# Convert Digits to Words

phone_number = input("Phone: ")
number_words = ""

for number in phone_number:
    if number == "1":
        number_words += "one "
    if number == "2":
        number_words += "two "
    if number == "3":
        number_words += "three "
    if number == "4":
        number_words += "four "
    if number == "5":
        number_words += "five "
    if number == "6":
        number_words += "six "
    if number == "7":
        number_words += "seven "
    if number == "8":
        number_words += "eight "
    if number == "9":
        number_words += "nine "
    if number == "0":
        number_words += "zero "
print(number_words)

#OR

digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output_str = ""

for character in phone_number:
    output_str += digits_mapping.get(character, "!") + " "

print(output_str)