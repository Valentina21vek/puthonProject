# 03/14/2021 If statement (continue)
num = 20

if num >= 1 and num <=10:
    print(f"TRUE number is equal or greater than 1 and less than 10")
else:
    print(f"FALSE number is less than 1 and greater 10")
##########exprrssion ANF/OR expression AND/OR expression#############

#OR:
##expression1 OR expression2 = True OR False it will return True
#AND
##expression1 AND expression2 = True OR False it will return False

age = 3
if 0 <= age <= 4:
    print ("Your admission is $0.")
elif 4 < age < 18:
    print ("Your admission cost is $5.")
elif 18 <= age < 140:
    print ("Your admission cost is $10.")
else:
    print ("Invalid age was entered, bye!")

age = int(input("enter the visitor age:"))
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print ("Invalid age was entered, bye!")
print(f"Your addmission cost is ${price}.")
# Exercise 5-3
alien_color = input("enter the alien_color (green,yellow,red)")
if alien_color == 'green':
    print(f"You just earned 5 points!")
elif alien_color == 'yellow':
    print(f"You just earned 2 points, whee!")
elif alien_color == 'red':
    print(f"You just earned 10 points,you are killing it, man!")
else:
    print(f"no points, sorry, take a rest, meditate!")
####-------------------######
friends = ["Dan"]
if friends:
    print(f"Good for you, Can I be your friend?")
else:
    print(f"Go out make some friends, only good friend!")
print("******** Using Multiple List ********************")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fires', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping.lower().strip() in available_toppings:
        print(f"I am adding {requested_topping.title().strip()}")
    else:
        print(f"Sorry, we dont have {requested_topping.upper().strip()}")

# Exercises:
# 1. Implement sum() with for loop
#    FuzzBuzz, assume user enter than number >0
#    print Fuzz if the number is dividable by 3
#    print Buzz if the number is dividable by 5
#    print FuzzBuzz if the number is dividible by 3 and 5

# H/W:
# Double characters in string (e.g. "abc" => "aabbcc")
# Prove that a numbert is a prime
# Prove that a string is a palindrome (mom,dad,

# % - modulus operator to return remainder in division
# // - floor division - division ignoring remainder and considiring only dividable num

num = int(input("enter the number > 0 :"))
if (num % 3 == 0) and (num % 5 == 0):
    print(f"FuzzBuzz your number {num} dividable by 3 and 5")
elif (num % 3 == 0):
    print(f"Fuzz your number {num} dividable by 3")
elif (num % 5 == 0):
    print(f"Buzz your number {num} dividable by 5")


