# Exercise 6.1
person_1 = {'first_name': 'alina', 'last_name': 'silver', 'age': '32', 'city': 'Moscow'}
print(f"Hi, {person_1['first_name'].title()}, is it {person_1['last_name'].title()} your last_name? Omg, {person_1['first_name'].title()}, you don't looks like you are {person_1['age']} years old!?")
person_1 ['country'] = 'Rashka' # add new value
print(person_1)
person_1 ['country'] = 'Russia'# modifie value
print(person_1)
del person_1 ['country'] # removing value (elements)
print(person_1)

fav_numbers = {'alina': '5', 'dina': '22', 'jane': '13'}
print (fav_numbers['alina'])

for key in fav_numbers:
    print(f"Hi, my Favorite number is also {key}!")
if  '13' in fav_numbers.values():
    print('Yes!')
