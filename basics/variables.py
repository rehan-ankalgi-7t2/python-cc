'''
Variable rules in python:
- case sensitive
- must start with a letter or an underscore
- can have number but cannot start the variable name with a number
'''

# all the allowed variable formats with definition and initialization

x = 1
y = 3.4
name = "John"
is_admin = True


# multiple assignment

x,y,name,is_admin = (1, 3.4, "John", True)

a = x + y

print(x, y, name, is_admin, a)

# type checking
print(type(x))

# type casting
x = str(x)
y = int(y)
z = float(y)
print(type(x), x)
print(type(y), y)