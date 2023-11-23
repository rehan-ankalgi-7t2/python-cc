'''
@IMPORTANT
@DEFINITION - a dictionary is a built-in data type that represents an unordered collection of key-value pairs. Dictionaries are also known as associative arrays or hash maps in other programming languages.
'''

# Creating Dictionaries:
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Accessing values:
name = my_dict['name']
age = my_dict['age']
print(name, age)

# Modifying values:
my_dict['age'] = 31
print(my_dict)

# copying Dictionary
your_dict = my_dict.copy()
print(your_dict)
 
# Adding and Removing Key-Value Pairs:
# You can add new key-value pairs using the assignment operator and remove key-value pairs using the del keyword.
my_dict['gender'] = 'Male'  # Add a new key-value pair
print(my_dict)
del my_dict['city']         # Remove a key-value pair by key
print(my_dict)

# Dictionary Methods:
# Dictionaries have various built-in methods for common operations, including keys(), values(), and items().
keys = my_dict.keys()      # Get a list of keys
values = my_dict.values()  # Get a list of values
items = my_dict.items()    # Get a list of key-value pairs as tuples
print(keys, values, items)

# Checking Key Existence:
# You can check if a key is present in a dictionary using the 'in' keyword.
is_present = 'age' in my_dict
print(is_present)

# Iterating over a dictionary
for key in my_dict:
    print(key, my_dict[key])

# Alternatively, using items()
for key, value in my_dict.items():
    print(key, value)

# Dictionary comprehensions
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

# Dictionaries are versatile and widely used in Python for tasks that involve associating values with keys. They are particularly useful when you need to represent structured data or create mappings between related pieces of information.