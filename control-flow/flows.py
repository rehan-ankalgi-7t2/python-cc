'''
@DEFINITION - loops are used to repeatedly execute a block of code. The two main types of loops in Python are for and while.
'''

# FOR LOOP:
# The for loop is used for iterating over a sequence (that is either a list, tuple, dictionary, string, or range).
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# WHILE LOOP:
# The while loop is used to repeatedly execute a block of code as long as a specified condition is true.
i = 0
while i < 5:
    print(i)
    i += 1

# CONTROL LOOP STATEMENTS
# 1. break Statement:
# The break statement is used to exit the loop prematurely.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# 3. else Clause with Loops:
# Both for and while loops can have an else clause. The code in the else block is executed if the loop condition becomes false.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
else:
    print("Loop finished")

# Nested Loops:
# You can use loops inside other loops.
for i in range(3):
    for j in range(2):
        print(i, j)


