# 03/20/2021 Lopping through Dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in my_car:
    print("-------------------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is : {my_car[key]}")
print("Example 2------------")
for key in my_car.keys():
    print("---------2----------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is : {my_car[key]}")
# if 'model' in my_car.keys():
if 'model' in my_car:
    print(f"Yes my_car desc contains model information")
print("Example 3------------")
for value in my_car.values():
    print("-------------------------------")
    print(f"value in this iteration is: {value}")

print("Example 4------------")
for val1, val2 in my_car.items():
    print("-------------------------------")
    print(f"val1 of this key is: {val1}")
    print(f"val2 of this key is: {val2}")
if 1964 in my_car.values():
    print(f"Yes my_car desc contains 1964 value(information)")

print("************example with list sort(), sorted(list)*************")
friends = ['john', 'jane']
print(friends)
sorted_friends = sorted(friends)
friends.sort() #
favorite_languages = {'jen':'python','sarah': 'c','edward': 'ruby','phil': 'python'}



# Exercise 6-4
rivers = {'nile': 'egypt', 'tigers': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through the {country.title()}.")

countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = [ companies, cities, countries]
print(customers)
print(customers[0])
print(customers[0][0])
print(f"printing barcelona: {customers[1][2]}")

multi_dim_nums = [
    [3,9,0],
    [2,7,1],
    [0,1,0]
]
print(f"printing the middle value {multi_dim_nums[1][1]}")

print("Nested Loops: looping through multidimensional list(array).")
for column in customers:
    print(column)
    # ['level up','abc company','ola company']
    for value in column:
        print(value.upper())
for city in customers[1]:
    print(city, end='\t')
print ("************* list of dictionaries*************")
user_0 ={'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 ={'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 ={'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = [user_1, user_0, user_2]
print(users[0])
print(users[2]['name'])
print(users[2]['age'])
print(users[2]['city'])

for user in users:
    print(users[2]['name'])
    print(users[2]['age'])
    print(users[2]['city'])

print ("---------looping--------")
for user in users:
    print(users[2]['name'], end=' || ')
    print(users[2]['age'],end=' || ')
    print(users[2]['city'],end=' || ')

print ("*************List in a Dictionary**************")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = {
    'countries': ['usa', 'russia', 'spain'],
    'cities': ['new york', 'moscow', 'barcelona'],
    'companies': ['level up', 'abc company', 'ola company']
}
print (customers['cities'])
print(customers['cities'][1])



print ("*************Dictionary in a Dictionary**************")
user_0 ={'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 ={'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 ={'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'mark', 'age': 35, 'city': 'tokyo'}
}
print(users)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)