"""

Given two sorted lists, write a Python code to merge them into a single sorted list.
"""


def sort(lst):
    temp = 0
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            temp = lst[i + 1]
            lst[i + 1] = lst[i]
            lst[i] = temp

            sort(lst)
    return lst


# my_list1 = [10, 20, 30, 40, 50, 60, 70, 80]
# my_list2 = [5, 15, 25, 35, 45, 55, 65, 75, 85]

a = [1, 4, 6, 7, 8, 12]
b = [10, 14, 22, 34, 56, 78, 99, 100]

merge_list = a + b

result = sort(merge_list)
print(result)
