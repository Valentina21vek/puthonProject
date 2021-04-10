# Lists (Array)
# Operations: create, access, add element, remove element, copy
# List_name = [] - creating an empty list
# List.append(newValue)
# List.insert(ind, value)
# del list(ind)
# list.remove(value)
# list.pop() -removes and return the last element, list.pop(ind)
# list(ind) = value  -assigning a new value to existing Index
# sorted(list) - copies the list and returns sorted copy of the list
# list.reverse()
# len.(list) - returns the length of your list(how big is list, i.e. number of elements)
# list[-n] - index start from the end of the list, last element is list [-1]

# creating list
from audioop import reverse

num_list = []
odd = 11
odds = [1,3,5,7,9,253]
# index:  0 1 2 3 4 5
# neg ind-6-5-4-3-2 -1
# 5 elements, size of "odds" list is 5
# what is the element on index 2? it is 5, because indexing start with 0
friends = ['jackson', 'said', 'lenur', 'tyson']
print(friends [0])

# Access
first_friend = friends[0]
print(f"friends: {friends}")
print(f"first_friend: {first_friend}")
print(f"friends[0]: {friends[0]}")
print(f"friends[1]: {friends[1]}")
print(f"friends[2]: {friends[2]}")
print(f"friends[3]: {friends[3]}")

print(friends [0].title())
print(friends [1].upper())
print(friends [2])
print(friends [3])

print(friends [-1]) # look at the right side of your list, negative indexes starting
print(f"frinds[-3]:{friends [-3].title()}")
print(f"odds[-3]:{odds [-3]}")

# Adding elements:
# list.append(new_element) - this adds new_element to the end of list
# list.insert(index, new_element) - this adds new_element on the indicated index, shift all elements to right
# add a friend: 'Obama' to a friend list
friends.append('obama')
print(f"new friends list: {friends}")
friends.insert(0,'messi')
friends.insert(1,'ronaldo')
print(f"new friends list after insert: {friends}")

# Resetting the existing element, only  existing index should be used
friends[2] = 'mark'
print(f"new friends list after resetting: {friends}")

# Removing the elements: by value, by index
friends.remove('mark')
print(f"new friends list after removing 'mark': {friends}")

removed_friend = []
removed_one = friends.pop(4)
friends.pop(4) # pop() function return (inform) what is removing
print(f"new friends list after popping index  '4': {friends}")
print(removed_one)

del friends[-1]
print(f"new friends list after del index -1: {friends}")

# friends = [] will redefining list to empty

cars = ['BUGHATI','FERRARI', 'Tesla', 'BMW']
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")

#3-4 guest_list = []
guest_list = ['jackson', 'said', 'lenur', 'tyson']
print(f"Hi {guest_list[0].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {guest_list[2].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {guest_list[1].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {guest_list[3].title()}, I would like to invite you to family dinner tomorrow.")

removed_guest = guest_list.pop(3)
print(f"I am sorry {removed_guest},see you next time")

guest_list.insert(3, 'akmal')

print(f"Hi {guest_list[3].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {guest_list[0].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[1].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[2].title()}, I would like to invite you to family dinner tomorrow!")
guest_list.insert(0, 'john'.title())
guest_list.insert(2, 'steven'.title())
guest_list.append('jennifer'.title())
print(guest_list)
print(f"Hi {guest_list[0].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[1].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[2].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[3].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[4].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[5].title()}, I would like to invite you to family dinner tomorrow!")
print(f"Hi {guest_list[6].title()}, I would like to invite you to family dinner tomorrow!")

print(f"Hi,{guest_list.pop(1).title()} ,I'm sorry I can't invite you to dinner")
print(f"Hi,{guest_list.pop(2).title()} ,I'm sorry I can't invite you to dinner")
print(f"Hi,{guest_list.pop(4).title()} ,I'm sorry I can't invite you to dinner")

print(guest_list)
removed_guests = []
removed_guests.append(guest_list.pop())
print(f"{removed_guests[-1].title()} ,I'm sorry I can't invite you to dinner")

removed_guests.append(guest_list.pop(0))
print(f"{removed_guests[-1].title()} ,I'm sorry I can't invite you to dinner")


print(removed_guests)
print(guest_list)

############ORGANIZING THE LIST########################
# 1.Sorting the list permanently
names =['lena', 'nicole', 'amina', 'sophia', 'jade']
print(names)
names.sort() # will change the list sorting an ascending order
print(names)
names.sort(reverse=True) # changing the list sorting in descending order
print(names)

# 2.Sorting the list temporarily and returning the copy of sorted list

cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars_asc = sorted(cars) # copy of the list started in asc order
sorted_cars_desc = sorted(cars, reverse=True) # copy of the list started in desc order
print(f"cars: {cars}")
print(f"sorted_cars_asc: {sorted_cars_asc}")
print(f"sorted_cars_desc: {sorted_cars_desc}")

cars.reverse()
print(f"cars: {cars}")
sorted_cars_asc2 = sorted(cars) # copy of the list sorted in asc order
print(f"sorted_cars_asc2: {sorted_cars_asc2}")

# abstract thinking is tested on solving some coding problem
list_size = len(cars)
print(f"list_size: {list_size}")
print(f"len('toyota  '): {len('toyota')}")
print(f"len('toyota  '): {len('toyota ')}")
print(f"len('toyota  '): {len('toyota  ')}")

vacation = ['Dominican', 'Mexico', 'Turkey', 'Malaysia']
print(f"vacation_list:{vacation}")
sorted_vacation = sorted(vacation)
sorted_vacation_desc = sorted(vacation, reverse=True)
print(f"sorted_vacation:{sorted_vacation}")
print(f"original_vacation_list: {vacation}")
print(f"reverse_order_vacation: {sorted_vacation_desc}")
print(f"original_vacation_list: {vacation}")
vacation.reverse()
print(f"vacation_after_reversing:{vacation}")
vacation.reverse()
print(f"vacation_after_reversing2:{vacation}")
vacation.sort()
print(f"vacation_after_sorting:{vacation}")
vacation.sort(reverse=True)
print(f"vacation_after_sorting_desc:{vacation}")

list_size = len(guest_list)
print(f"number_of_guests: {list_size}")

# None:null is in SQL
# object : everything is an object in the python (character,file,string,variable,list,function etc.)
# iterable : something that can iterate(loop) most data structures,string,not a number,not boolean
# return statement:some functions return an object so we can use in print to bring up to the STDOUT(console),but some functions do not return anything (None) so result of the






