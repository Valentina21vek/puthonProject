# naming the file: avoid spaces, avoid upper cases,'_' can be used to separate words
# new_variables.py (python), newVariables.java (java)
# Variables:
# naming : should not start with numbers, starts with lower case, symbols and numbers can be used
# nameofthevariable = value, declaring and define setting a value for the variable
# Data types: Strings(str), Integers(int), Boolean(bool), Floats(float)
vname = 'John Doe' # String data type
num = 12 # Integer data type
status = True # Boolean data type
price = 45.789 # Double/Float data type
message = "Hello class, we are starting to learn Python!!!"

print("Hello Again!")
print(vname)
print(num)
print("---------------")

vname = 'Jane Doe' # I am resetting the value of vname variables
num = 9876
print(vname,"***", num, status, price, message)
a = 'John'
b = 5 # instead b better use num1
c = 10 # instead c better use num2

# Exercise 2.1
message = "Exercises are very helpful!"
print(message)
# Exercise 2.2
message = "Exercises are very helpful and useful!"
print(message)

# CTRL + D - duplicate the line that your cursor is on
# CTRL + C - copy the line that your cursor is on,you don't need to highlight
# CTRL + v - paste the copied contest to the next line
# Shift +Alt + Up/Down - take the line your cursor is on Up/Down
# ctrl + / will take you where the specific variable is defined
vname = 'Eric'
# message = "Hello" + " " + vname +",would you like to learn some Python today? "
print(message)

vname = 'john doe'
print(vname.upper())
print(vname.lower())
print(vname.title())

message1 = 'Albert Einstein said,'
message2 = '"A person who never made a mistake never tried anything new."'
famus_person = 'Albert Einstein'
message = 'said,'
print('\t\t\t' + message1 + message2)
print(famous_person + " "+ message + message2)
vname = ' John Doe '
print(vname)
vname = vname.rstrip()
print(vname)
vname = vname.lstrip()
print(vname)




