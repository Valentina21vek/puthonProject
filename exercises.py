def favorite_book(book_title):
    print(f"One of my favorite books is '{book_title}'")


favorite_book("Alice in Wonderland")

def multiplication(num1: int, num2: int):
    num3 = (num1 * num2)
    print(f"multiplication {num1} * {num2} will be {num3}")
multiplication(4, 5)
multiplication(6, 6)

def swap(a, b):
    print(f"the value of a is: {a}")
    print(f"the value of b is: {b}")
    temp = a
    a = b
    b = temp
    print(f"the value of a is: {a}")
    print(f"the value of a is: {a}")

def great_user2(name, lastname):
    print(f"Welcome {name.title()} {lastname.title()}!")

great_user2('valentina', 'kim')

a = 45
b = 78
a, b = b, a
print("a =",a)
print("b =",b)

for num1 in range(1,2):
  for num2 in range(1,11):
    print(f"{num1} * {num2} = {num1*num2}")


for num1 in range(2,3):
  for num2 in range(1,21):
    print(f"{num1} * {num2} = {num1*num2}")
  print()
  print()

for num in range(1,11):
    print(num, end= '\t')
print('\n----------------------------------------')
for num2 in range(1,2):
    for num3 in range(1,11):
        print(num3, end= '\t')
print()
print()
print()

for num in range(2,21):
    print(num, end= '\t')
print('\n-------------------------------------------------------------')
for num2 in range(2,21):
    for num3 in range(2,3):
        print(num2*num3, end= '\t')
print()




def multiply(num1: int, num2: int):
    num3 = (num1 * num2)
    print(f" {num1} * {num2}= {num3}")
multiply(1, 10)
multiply(2, 20)
