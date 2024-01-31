"""
Make your own list. Write a Python program that takes an integer as an input,
and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.

"""

import random


def listSlicing(lst, num):
    lst1 = lst[len(lst) - num :]
    lst1.reverse()
    return lst1


my_list = [random.randint(1, 50) for x in range(12)]
print(f"Original List is : {my_list}")
n = int(input("Enter the poistion of list to be sliced: "))

result = listSlicing(my_list, n)
print(f"List after Slicing: { result}")
