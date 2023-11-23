'''
@DEFINITION - a lambda function is a small, anonymous function defined using the lambda keyword. Lambda functions are often used for short, simple operations where a full function definition would be overkill.
@SYNTAX - lambda arguments: expression
'''

# example of a lambda function:
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
lambda_add = lambda x, y: x + y

print(add(2, 3))         # Output: 5
print(lambda_add(2, 3))  # Output: 5


