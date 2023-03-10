weight = float(input("What is your weight? "))
unit = input("What units? (L)bs or (K)gs?")

if unit.upper() == "L":
    converted = weight * 0.45359237
    print(f"You are {converted} kilos")
elif unit.upper() == "K":
    converted = weight * 2.20462262185
    print(f"You are {converted} pounds")
else:
    print("Please enter a L or K for units.")