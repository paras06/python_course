"""
Write a python program which prints all the values whose count is
greater than 3. (Make sure to make a list with at least 15 numbers)
Store them in another list using list comprehension

"""

import random

lst1 = [
    34,
    96,
    34,
    65,
    51,
    27,
    96,
    96,
    11,
    34,
    34,
    34,
    51,
    51,
    51,
    51,
]

result = []

lst2 = [result.append(i) for i in lst1 if (lst1.count(i) > 3 and i not in result)]
print(result)
