"""
Create a function findLargest
that accepts an List of Integers and returns the largest number from the list.

"""


def findLargest(my_list):
    largest = my_list[0]
    for i in range(0, len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


lst = [34, 11, 91, 59, 33, 22]
result = findLargest(lst)
print(result)
