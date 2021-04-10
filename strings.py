# 03/04/2021

# String(str)
# Function available for string
fullname = "john doe"
print(fullname)
print(fullname.upper())
print(fullname.title())
msg = "we are the Losers"
print(msg.replace('Losers','champions').title())

# Concatenation
msg1 = fullname.title() + " " + msg + "!!!"
print(msg1)

# working with Whitespaces in string: \t, \n,
msg1 = fullname.title() + "\t, " + msg + "!!!"
print(msg1.replace('\t', ''))
msg2 = fullname.upper() + "\n\t\t\t, " + msg
print(msg2)
msg3 = '\n\t\t\t' + fullname.title() + ", " + msg
print(msg3 + '!!!')
msg4 = f" {fullname.title()}, {msg}"
print("fstring")
print(msg4 + '!!!')

num = 456
# print(num.strip()) -error string strip is used only for string data type

message = "One of Python's strengths is its diverse community"
print(message)

num = 456
num2 = 600
print(num + num2)
print(num2 - num)
print(num * num2)
print(num / num2)

print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")

print("Value of num is : " + str(num))
# str(expression - this will convert the data type to str
print("num + num2 = " + str(num + num2))
num3 = "753"
# print(f"num + num3 =  + {num + num3}") -error
print(f"num + num3 = {num + int(num3)}") # not error

message1 = 'Albert Einstein said,'
message2 = '"A person who never made a mistake never tried anything new."'
famus_person = 'Albert Einstein'
message = 'said,'
print('\t\t\t' + message1 + message2)
person = "Albert Einstein"
quote = f'\t\t\t {person} once said, {message2}'
print(quote)











