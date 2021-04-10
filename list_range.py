# 03/11/2021

cars = ['bughatti', 'ferrari', 'tesla', 'lexus']
# Making Numerical list
for num in range(4):
    print(num)
# Shift +f6 - shortcut for Refactor>rename
# Ctrl + Y - delete the line
nums = range(4) # this does not mean nums list = [0,1,2,3]
print(nums)
nums2 = list(range(4)) # this create list data structure from sequence of numbers
print(nums2)
for num in nums2:
    print(num)
for num in range(1, 4): # print range from start(1) to stop(3)
    print(num)
for num in range(4):
    print(f"number:{num}")
print("range with start,stop and step ---")
for num in range(1,10,2):
    print(num)
for num in range(1,20,3):
    print(num)
print("range all even number from 1 to 16 (16 should be included")
evens = []
for num in range(2,17, 2):
    print(num)
    evens.append(num)
    print(evens)
print(f"This is final list: {evens}")

print("Exercise2: print the squares of numbers from 10 to 20")
for num in range(10,21):
    print(num**2) # or print(num*num)
squares = list()
for num in range(10,21):
    squares.append(num**2)
print(squares)

print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

cars = ['Bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}") # this ind is expression

cars = ['Bugatti', 'ferrari', 'tesla', 'lexus']
cars_len = len(cars)
print("looping the list using index************")
for ind in range(cars_len): # or for ind in range(len(cars)):
    print(ind)
    print(f"index of the {cars[ind]} is {ind}") # this ind is a values
#-----------------------------------------------------------------
print("# List comprehension : ")
squares = list()
for num in range(10,21):
    squares.append(num**2)
squares = [num ** 2 for num in range(10,21)] # for read only now, use later
print(squares)

print("Exercise 4-4, 4-5: One Million: ***************************")
nums = []
for num in range(1,1000000):
    print(num)
    nums.append(num)
    print(num)
print(f"smallest : {min(nums)}")
print(f"biggest : {max(nums)}")
print(f"total : {sum(nums)}")

num2 =[]
squares2 = [num**2 for num in range(1,5)]
print(f"squares:{squares2}")