'''
@DEFINITION - functions are blocks of reusable code that perform a specific task. Functions help in organizing code into modular and manageable pieces, making the code more readable and maintainable.
'''

# Defining the functions:
# You can define a function using the def keyword, followed by the function name, parameters in parentheses, and a colon. The function body is indented.
def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")

# Function Parameters:
def add_numbers(a, b):
    """This function adds two numbers."""
    return a + b

result = add_numbers(5, 7)
print(result)  # Output: 12

# Return Statement:
def square(x):
    """This function returns the square of a number."""
    return x ** 2

result = square(4)
print(result)  # Output: 16

# Default Params:
# You can provide default values for parameters, making them optional when calling the function.
def power(base, exponent=2):
    """This function calculates the power of a number with a default exponent of 2."""
    return base ** exponent

result1 = power(3)
result2 = power(3, 4)
print(result1, result2)  # Output: 9 81

# Keyword Arguments:
# You can use keyword arguments to specify values for parameters by their names.
def person_info(name, age, city):
    """This function prints information about a person."""
    print(f"Name: {name}, Age: {age}, City: {city}")

person_info(age=25, name="John", city="New York")

# Variable Number of Arguments:
# You can use *args and **kwargs to accept a variable number of positional and keyword arguments.
def print_arguments(*args, **kwargs):
    """This function prints all passed arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_arguments(1, "two", 3.0, name="Alice", age=30)
