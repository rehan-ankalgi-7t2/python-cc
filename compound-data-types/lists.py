'''
@IMPORTANT
@DEFINITION - a list is a built-in data type that represents an ordered, mutable (changeable), and iterable collection of elements., Allows duplicate members
'''

# create list
numbers = [1, 2, 3]
fruits = ["Apple 🍎", "Litchi 🍒", "Kiwi 🥝"]

# create using constructor function
numbers2 = list((1, 2, 3))

print(numbers, numbers2)
print(fruits)
print(len(fruits))
print(fruits[1])

# append to list
fruits.append("Mango 🥭")
print(fruits)

# change the value
fruits[1] = "Banana 🍌"

# remove from list
fruits.remove("Mango 🥭")
print(fruits)

# insert into a position in list
fruits.insert(1, "Strawberry 🍓")
print(fruits)

# remove with pop()
fruits.pop(2)
print(fruits)

# reverse the list
fruits.reverse()
print(fruits)

# sort the list
fruits.sort()
print(fruits)

# reverse sort the list
fruits.sort(reverse=True)
print(fruits)

# list slicing
sub_fruits = fruits.slice[1:2]
print(sub_fruits)

# list comprehension
squares = [x**2 for x in range(5)]
print(squares)