# my_module.py
import re

def greet(name):
    print(f"Hello, {name}!")

def square(x):
    return x ** 2

def emailValidator(emailString):
    if len(emailString) > 7:
        return bool(re.match("^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$", emailString))