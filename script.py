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
If/Else In A Comprehension
"""
# Categorize numbers as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)
