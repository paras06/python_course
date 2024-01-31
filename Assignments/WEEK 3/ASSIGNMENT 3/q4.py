"""
Create a function findSmallest
that accepts an List of Integers and returns the smallest number from the list.

"""


def findSmallest(my_list):
    smallest = my_list[0]
    for i in range(0, len(my_list)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest


lst = [34, 11, 91, 59, 33, 22]
result = findSmallest(lst)
print(result)
