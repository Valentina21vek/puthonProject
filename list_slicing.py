# 03/13/2021
# Working with part of the list
cars = ['bughatti', 'ferrari', 'tesla', 'lexus']
# slice of the list list_name[start:stop] - start is inclusive,stop is exclusive
# values: list_name[start], list_name[start+1]
for car in cars[1:2]:
    print(f"the car is: {car}")
print("-------second---------")
for car in cars[:3]: #this same things as cars[0:3]
    print(f"the car is: {car}")
print("-------third---------")
for car in cars[2:]: #this same things as cars[2:end of the list]
    print(f"the car is: {car}")
print("-------fourth---------")
for car in cars[2:10]:  # this same things as cars[2:10]
    print(f"the car is: {car}")
print("-------copying&linking---------")
print("-------linking the variables to the same value----------")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")

print("-------copying---------")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('toyota')
print(f"cars: {cars}")
print(f"cars3: {cars3}")

print(f"This first three items in the list are: {cars[:3]}")
print(f"Three items from the middle of the list are: {cars[2:5]}")
print(f"The last three items in the list are: {cars[3:]}")

# Lists can be modified
# Tuples - data structure similar to list but cannot be modified (immutable)
cars_t = ('bughatti', 'ferrari', 'tesla', 'lexus')
print(f"first value is : {cars_t[0]}")

cars[0] ='honda' # this is possible since cars is the list data structure
# cars_t[0] = 'honda' #this is not possible since the cars_t is tuple d/s
print(f"first value is : {cars_t}")

cars_t = ('honda','ferari', 'tesla')
print(f"cars_t: {cars_t}")
print(f"size of tuple:{len(cars_t)}")


