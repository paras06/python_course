"""
Write a Python program to get the 4th element from the last element of a tuple.

"""

import random


def get_fourth_from_last(t):
    if len(t) >= 4:
        return t[-4]
    else:
        return "Tuple is too short"


# my_tuple = [random.randint(1, 50) for x in range(12)]
my_tuple = (8, 46, 23, 42, 21, 17, 50, 13, 10, 6, 46, 41)
print(
    f"4th element from the last element of given tuple is: {get_fourth_from_last(my_tuple)}"
)
