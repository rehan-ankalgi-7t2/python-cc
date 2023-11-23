name = "rahul"
age = 25

# concatenation
print("hello my name is " + name + " and i am " + str(age))

#arguements by position
print("hello my name is {name} and I am {age}".format(name=name, age=age))

# F-Strings
print(f"hello my name is {name} and I am {age}")

# STRING METHODS

s = "hello anaconda"

# capitalize
print(s.capitalize())

# upper case
print(s.upper())

# lower case
print(s.lower())

# case swapping
print(s.swapcase())

# length of a string
print(len(s))

# Replace a string
print(s.replace("hello", "goodbye"))

# count a character frequency
print(s.count("a"))

# returns true if the string starts with...
print(s.startswith("hello"))

# returns true if the string ends with...
print(s.endswith("dingo"))

# split the string into a list
print(s.split())

# find the position of a character in the string
print(s.find('r'))

# check if the string has all alphanumeric characters
print(s.isalnum())

# check if the string has all alphabetic characters
print(s.isalpha())

# check if the string has all numeric characters
print(s.isnumeric())