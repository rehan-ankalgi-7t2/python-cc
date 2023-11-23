'''
@IMPORTANT
@DEFINITION - a set is an unordered, mutable collection of unique elements. Sets are defined using curly braces {} or the set() constructor
'''

# Creating sets:
my_set = {1, 2, 3, 4, 5}
another_set = set([3, 4, 5, 6, 7])
# Note that sets automatically remove duplicate elements, so the resulting set will only contain unique values.

# Adding and removing elements:
my_set.add(6)     # Add an element
my_set.remove(3)  # Remove a specific element (raises an error if the element is not present)
my_set.discard(3) # Remove a specific element (ignores the error if the element is not present)

# Set operations:
union_set = my_set | another_set                    # Union of sets
intersection_set = my_set & another_set             # Intersection of sets
difference_set = my_set - another_set               # Set difference
symmetric_difference_set = my_set ^ another_set     # Symmetric difference

print (union_set)
print (intersection_set)
print (difference_set)
print (symmetric_difference_set)

# Membership test:
is_present = 3 in my_set
print(is_present)

# Iterating over sets
for element in my_set:
    print(element)

# Set comprehension
squares_set = {x**2 for x in range(5)}
print(squares_set)

# Clear sets
squares_set.clear()
print(squares_set)

# Delete Sets
del squares_set
# NameError: name 'fruits' is not defined