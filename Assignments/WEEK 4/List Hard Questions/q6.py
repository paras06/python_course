"""
Write a Python code to find the difference between two lists (i.e., elements present in the first list but not in the second).

First list = [1,2,9] second list = [8,7,9]

difference between first list and second list = [1,2]


difference_result = [item for item in first_list if item not in second_list]

"""


def find_difference(lst1, lst2):
    result = []
    for i in lst1:
        if i not in lst2:
            result.append(i)
    return result


first_list = [1, 2, 9, 88, 45, 29, 65, 94, -32, 45]
second_list = [8, 7, 9, 99, 87, 94, 29, 0, -31]

result = find_difference(first_list, second_list)
print(f"Difference between first list and second list: {result} ")
