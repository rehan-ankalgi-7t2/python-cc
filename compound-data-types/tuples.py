'''
@IMPORTANT
@DEFINITION - a tuple is a built-in data type that is similar to a list but has some key differences. Like lists, tuples are used to store collections of items. However, there are a few important distinctions, Allows duplicate members

@IMMUTABILITY - Tuples are immutable, meaning their elements cannot be changed or modified after the tuple is created. Once a tuple is defined, you cannot add, remove, or alter elements.

@SYNTAX - Tuples are defined using parentheses () instead of square brackets [] used for lists.
'''

# create tuple
numbers = (1, 2, 3)
fruits = ("Apple 🍎", "Litchi 🍒", "Kiwi 🥝")

# trailing comma to be left in the single tuple
fruits2 = ("Apple 🍏",)     # <class 'tuple'>
# fruits2 = ("Apple 🍏")      # <class 'str'>
print(fruits2, type(fruits2))

# create using constructor function
numbers2 = tuple((1, 2, 3))

# tuples are unchangeable
# fruits[2] = "Banana 🍌"
# print(fruits) 
# # TypeError: 'tuple' object does not support item assignment

print(numbers, numbers2)
print(fruits)
print(len(fruits))
print(fruits[1])

# delete a tuple
del fruits
# print(fruits)
# NameError: name 'fruits' is not defined

# slicing tuples
fastFood = ("Pizza 🍕", "Beacon 🍔", "Soda 🥤", "Fries 🍟")
sides = fastFood[2:]
print(sides)