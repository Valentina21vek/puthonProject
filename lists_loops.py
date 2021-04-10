# Loops - process of iteration,going through the elements, create repetitive actions
# Flow control
# Syntax in python language(for loop):
# for variable in list_of_elements:
#    repetitive code here
import really as really

cars = ['BUGATTI','FERRARI', 'Tesla', 'BMW']
for car in cars:
    print(f"I would like to own a {car.title()} car.")
# colon at the end of "for' Line
# 'in' in the 'for" line
# give any name to a variable and use that variable inside ONLY the for loop code
# lines of code that belong to for loop(repetitive code) must be indented
# indentation in loop = 1tab( 4 spaces)

states = ['New York', 'New Jersey', 'Florida', 'California']
for state in states:
    print(f"Welcome to {state.title()} , Enjoy your trip!")
# states>> 4 members >>
#       >>1st loop/round >> state = 'New York'
#       >>print (f"Welcome to {state.title()}!!!")
#       >>Welcome to New York!!!

#       >>2nd loop/round >> state = 'New Jersey'
#       >>print (f"Welcome to {state.title()}!!!")
#       >>Welcome to New Jersey!!!

pizzas = ['Cheese','Pepperoni','Fresh Mozzarella','Garden']
for pizza in pizzas:
    print(f"My favorit pizza is {pizza} !")
print('I really loves pizza!')
animals = ['dog', 'cat', 'fish', 'hamster', 'parrot']
for animal in animals:
    print(f"A {animals[0].title()} is the Best Friend!")
    print(f"A {animals[1].title()} is very cute!")
    print(f"A {animals[2].title()} needs to much water!")
    print(f"A {animals[3].title()} smells not good!")
    print(f"A {animals[4].title()} is too laud!")
animal = animals(range(1,6))
print(animal)

