name = input('What is your name? ')
print(f"Hello {name} ")

birth_year = input('What is your birth year ? ')
print(f"Oh nice, {birth_year} ")

print('Now I shall calculate your age! ')
current_year = input('What is the current year ? ')
age = int(current_year) - int(birth_year)
print(f"{age} years old ")

print('Now i will calculate your weight in kg from pounds(lbs)! ')
weight_lbs = input('Weight in lbs: ')
weight_kg = int(weight_lbs) * 0.45
print(f"you are currently {weight_kg} ")

practice = '''

Thanks for coming 
hope you had a great time here

with  respect,
  NIBRAS


'''


print(practice)