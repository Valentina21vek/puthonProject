
def greet_user():
    """this is a docstring, something that describe the function."""
    print("Hello!!!")
greet_user() # this is how we Call function

def greet_user_by_name(name): # (name) is requared parameter
    """it will say hello and use the name entered."""
    print(f"Hello, {name.title()}!")
greet_user_by_name('ali') # if doesnot choose (name) will be error

# 03/21/2021 Functions

def greet_user():
    """this is a docstring, something that describe the function."""
    print("Hello!!!")


def greet_user_by_name(name):
    """
    it will say hello and use the name entered.
    name is required parameter, user has to pass to a function
    """
    print(f"Hello, {name.title()}!")


def sum_numbers(num1, num2):
    print(f"sum of {num1} and {num2} is {num2 + num1}")
    print(f"square of the {num2} is : {num2 ** 2}")


# def describe_pet(pet='dog', pet_name ): always put required parameters first
def describe_pet(pet_name, pet='dog'):
    """
    Keyword argument is pet with default value
    :param pet_name:
    :param pet: it is pet type : dog, cat etc, optional param, default is dog
    :return:
    """
    print(f"I have a {pet} and we call it {pet_name.title()}")


#  ******************************************************
# All executions of the functions (Calling the functions)
greet_user()  # this is how you CALL function
# greet_user_by_name()  # expected TypeError
# greet_user_by_name('ali')
# sum_numbers(45, 78)
# sum_numbers(-46, 34)
# sum_numbers(num2=-46, num1=34)

describe_pet('Lazy', 'cat')
describe_pet('Fluffy', 'dog')
describe_pet('Fluffy')
describe_pet(pet='cat', pet_name='Pretty')
# describe_pet(pet='snake')  # TypeError: required parameter is missing





