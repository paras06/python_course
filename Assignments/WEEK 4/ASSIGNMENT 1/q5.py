"""
Write a python program to interchange first and last elements in a list

"""

import random


def listSlicing(lst):
    lst[-1], lst[0] = lst[0], lst[-1]
    # lst1 = lst[-1 * num :]
    return lst


my_list = [random.randint(1, 50) for x in range(12)]
print(f"Original List is : {my_list}")

result = listSlicing(my_list)
print(f"List after Slicing: { result}")
