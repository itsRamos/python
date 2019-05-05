# STRINGS ARE IMMUTABLE, so they cannot be changed

msg = "hello world"
print(msg)

# Method to capitalize the first letter of the string
print (msg.capitalize())

# method to change all letters to capitals
print(msg.upper())

# method to change all letters to lowercase
print (msg.lower())

# method to count how many letters are in a string
print (msg.count('o'))

# method to find the first ocurrence of a letter in a string
print (msg.find('o'))

# method to center a string in between a set amount of letters
print (msg.center(20,'z'))

# method to add a tab in between
print('hello\thi')

# method to add a tab in between
print('hello\thi'.expandtabs())

# method to see if all characters are alphanumeric
print(msg.isalnum())

#method to check if all characters are alphabetic
print(msg.isalpha())

# check it characters all lowercase
print(msg.islower())

# check if all chars are blank spaces
print(msg.isspace())

# check is chars form a title
print(msg.istitle())

# check if chars are all uppercase
print(msg.isupper())

n = 'HELLO'
print(n.isupper())

# check if string ends in a character
print(msg.endswith('o'))
print(msg.endswith('d'))

msg[-1] == 'o'
msg[-1] == 'd'

# string have some built in methods that can reflect regular expressionss

# split will return a list of the and split at every occurence
s = 'hello'
print (s.split('e'))

print (s.partition('e'))
