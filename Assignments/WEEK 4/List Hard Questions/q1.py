"""
Write a Python code to check if a given list is sorted in ascending order.

Input --
[10, 20, 30, 40, 50, 60, 70, 65]
Output--
Given List is not sorted!!

Input --
[10, 20, 30, 40, 50, 60, 65, 70]
Output--
Given List is sorted!!


"""


def isListSorted(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


my_list = [10, 20, 30, 40, 50, 60, 65, 70]
result = isListSorted(my_list)

if result:
    print("Given List is sorted!!")
else:
    print("Given List is not sorted!!")
