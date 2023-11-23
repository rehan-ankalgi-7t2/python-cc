'''
@DEFINITION - a module is a file containing Python definitions and statements. The file name is the module name with the suffix .py. Modules allow you to organize your code logically, break it into smaller files, and reuse code across different Python scripts or projects.
'''
import datetime
from time import time
import camelcase
from my_module import emailValidator

today = datetime.date.today()
print(today)

timestamp = time()
print(timestamp)

c = camelcase.CamelCase()
print(c.hump("hello there world"))

isEmailValid = emailValidator("webster@mw.com")
print(isEmailValid)