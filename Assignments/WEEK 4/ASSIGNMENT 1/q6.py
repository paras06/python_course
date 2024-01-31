"""
Write a Python code to split a list into two halves using list slicing. (Keep the length of list even).

"""

import random


def splitList(lst):
    lst_1 = lst[0 : (len(lst) // 2)]
    lst_2 = lst[(len(lst) // 2) :]
    return lst_1, lst_2


my_list = [random.randint(-50, 50) for x in range(12)]
print(f"Original List is : {my_list}")

result = splitList(my_list)
print(f"List after Slicing: { result}")
