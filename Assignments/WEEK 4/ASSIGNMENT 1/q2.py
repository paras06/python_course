"""
Make your own list of numbers. Ask a start and end position from User. 
Make another diff erent list which will contain number from start to end position. Use slicing logic.

"""

import random


def listSlicing(lst, start, end):
    lst1 = lst[start:end]
    return lst1


my_list = [random.randint(1, 50) for x in range(12)]
print(f"Original List is : {my_list}")
start = int(input("Enter the start poistion of list: "))
end = int(input("Enter the lst position of list: "))

result = listSlicing(my_list, start, end)
print(f"List after Slicing: { result}")
