"""
List comprehensions
"""


""" 
1) Basic List Comprehension

instead of writing this, use a list comprehension
that is easier to read
values = []
for x in range(10):
    values.append(x)

Using list comprehension, contains a for loop inside a list:
values = [x * x got x range(10)]
print(values) """

"""
Example 2: List comprehension with condition 
Example: get all the even numbers from 0 - 50

evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

evens = [number for number in range(50) if number % 2 == 0]
print(evens)
"""

"""
Example 3: Comprehension with multiple conditions

Strings that start with "a" and end in "y"

options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)

print(valid_strings)

# this is the same code, now written as a list comprehension:
valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]

print(valid_strings)
"""
"""
Example 4: Nested List Comprehension

# Flattening a matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []


for row in matrix:
    for num in row:
        flattened.append(num)
# "num for row in matrix" is exterior for loop, any
# for loops after that are interior for loops
flattened = [num for row in matrix for num in row]
print(flattened)
"""

"""
Example 5: If/Else In A Comprehension

# Categorize numbers as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)

# list comprehension with if/else:
categories = [
    "Even" if x % 2 == 0 else "Odd" for x in range(10)
]

print(categories)
"""

"""
Example 6: Nested list comprehension
"""

import pprint
printer = pprint.PrettyPrinter()

lst = []
# builds a 5x5x5 matrix or 3D list
""" for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)

    lst.append(l1) """

# this is what gets added inside of the list [[num for num in range(5)] for _ in range(5)]
# this tells Python the output is 5 lists with the numbers 0 through 4: [num for num in range(5)]
# this tells Python you will repeat this process times - for _ in range(5)
# the final list comprehension:
# lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]

# printer.pprint(lst)

"""
Example 7: Transformation in Comprehension
"""
# List comp with functions


def square(x):
    return x**2


# apply a function to a value inside a list comprehension
squared_numbers = [square(x) for x in range(10)]

"""
Example 8: Dictionary comprehension
"""

# Creating a dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
# dictionary comprehension
my_dict = {k: v for k, v in pairs}
print(my_dict)

"""
Example 9: Set comprehension
Removing duplicates from a list while applying a function.
"""

nums = [1, 2, 2, 3, 3, 4, 4, 4, 4]
# python knows this is a set comprehension
# if you don't have any key inside it:
unique_squares = {x**2 for x in nums}

"""
Example 10: Generator comprehension
A generator returns a value when needed,
gives the next value when asked for it
and is generated on the fly.
"""
# sum asks for each value sequentially and adds it to a sum that it's strong internally
# this is the generator comprehension: x**2 for x in range(1000000)
sum_of_squares = sum(x**2 for x in range(1000000))
# this uses a list and generates every possible value :
# sum_of_squares = sum([x**2 for x in range(1000000)])
print(sum_of_squares)
