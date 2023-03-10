import datetime

birth_year = input("Birth year: ")
print(type(birth_year))
today = datetime.date.today()
this_year = today.year
age = this_year - int(birth_year)
print(type(age))

print(age)