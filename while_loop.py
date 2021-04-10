# 03/21/2021 While Loop, Functions
print("******incrementing the variable to reach upper boundary******")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

print("******decrementing the variable to reach lower boundary******")
current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -=1

print("*********** Game Started ***********")
color = None
while color != 'quit' or color != 'q':
    color = input("Choose the color (green/yellow/red):")
    color = color.lower().strip()
    point = 0
    if color == 'quite' or color == 'q':
        break
    if color == "green":
        point = 15
    elif color == "yellow":
        point = 10
    elif color == "red":
        point = 5
    else:
        print("sorry, that's not a right color.0 point;")
    print(f"You have {point} points")
    break
print("closing the game...")


# 'hello guys'
count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print (f"number of l's is :{count}")


while True:
    number = input("choose the magic number:")
    if number == '99':
        break
    print (f"You entered number : {number}, try again!")
