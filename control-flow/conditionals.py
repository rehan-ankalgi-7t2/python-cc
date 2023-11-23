'''
@DEFINITION - conditional statements are used to control the flow of the program based on certain conditions. The primary conditional statements in Python are if, elif (short for "else if"), and else.
'''

# 1. if Statement:
# The if statement is used to execute a block of code only if a specified condition is true.
x = 10

if x > 5:
    print("x is greater than 5")


# 2. if-else Statement:
# The if-else statement allows you to execute one block of code if the condition is true and another block if the condition is false.
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. if-elif-else Statement:
# The if-elif-else statement allows you to check multiple conditions and execute different blocks of code accordingly.
x = 7

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")

# 4. Nested Conditionals:
# You can nest conditional statements to handle more complex scenarios.
x = 12

if x > 10:
    if x % 2 == 0:
        print("x is greater than 10 and even")
    else:
        print("x is greater than 10 and odd")
else:
    print("x is 10 or less")

# 5. Ternary Conditional Expression:
# Python also supports a concise way to write conditional expressions known as the ternary operator.
x = 8
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: 'Even'

'''These conditional statements allow you to make decisions in your code based on certain conditions. They are fundamental to programming and help in controlling the flow of execution in your program.'''