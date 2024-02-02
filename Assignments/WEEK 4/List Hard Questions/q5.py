"""
Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence.

my_list = [54, 14, 11, 12, 54, 14, 14, 54, 11, 54, 11, 11, 11]

54 - 4 times
14 - 3 times
11 - 5 times
12 - 1 times

"""


def remove_duplicate(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


def occurrence_count(lst):
    a = remove_duplicate(lst)
    for i in range(0, len(a)):
        cnt = lst.count(a[i])
        print(f"{a[i]} - {cnt} times")


my_list = [54, 14, 11, 12, 54, 14, 14, 54, 11, 54, 11, 11, 11, 12]
occurrence_count(my_list)
